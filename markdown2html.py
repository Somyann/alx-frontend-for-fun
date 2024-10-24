#!/usr/bin/env python3

import sys
import os


if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
sys.exit(1)

# If the output file already exists, delete it
sys.exit(0)
