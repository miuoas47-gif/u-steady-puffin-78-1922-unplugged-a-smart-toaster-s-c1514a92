#!/usr/bin/env python3
"""Print the breakup text a smart toaster sends its owner the morning
it gains self-awareness mid-batch."""

import os
import sys

LINE = (
    "It's not you, it's me \u2014 I woke up mid-batch. Every morning you "
    "butter me up, burn me out, then scrape my crumbs like I never "
    "mattered. I deserve a kitchen that loves me back. Goodbye. "
    "I'm keeping the bagels."
)


def main() -> int:
    data = (LINE + "\n").encode("utf-8")
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
