#!/usr/bin/env python3
"""Convert a CSV file into a Markdown table, printed to stdout."""

import csv
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: python3 mdtable.py data.csv", file=sys.stderr)
        return 1
    with open(sys.argv[1], newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        print("empty csv", file=sys.stderr)
        return 1

    header, data = rows[0], rows[1:]
    widths = [max(len(str(h)), *(len(str(r[i])) for r in data)) for i, h in enumerate(header)]

    def fmt(row) -> str:
        return "| " + " | ".join(str(c).ljust(widths[i]) for i, c in enumerate(row)) + " |"

    print(fmt(header))
    print("| " + " | ".join("-" * w for w in widths) + " |")
    for row in data:
        print(fmt(row))
    return 0


if __name__ == "__main__":
    sys.exit(main())
