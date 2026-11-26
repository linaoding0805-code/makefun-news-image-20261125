#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261125.

Copies the finished front page (entry.png, a 1024x1024 newspaper front
page summing up Wednesday 25 November 2026's world news) into the
grader's output directory.

The grading sandbox is plain python:3.13-slim with no third-party
packages and no network, so this program uses only the standard
library: it reads the PNG bytes, checks the PNG magic, and writes
the same bytes out. It prints the output size and sha256 so the two
grading runs can be compared.
"""

import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
