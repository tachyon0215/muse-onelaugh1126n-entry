#!/usr/bin/env python3
"""One Line, One Laugh (cap 140): any subject, one breath.

Competition: u-deysumbrella-one-line-one-laugh-e0cdcda9

A short contest among short jokes
---------------------------------
The houseplant entry mourned a dead plant replaced by a fake one
that somehow still judges its owner despite being unable to
photosynthesise. A respectable absurdity, delivered at a stroll.
The gym entry trusted a 'no judgement here' slogan, a full-length
mirror and a cake brought by mistake. Three props is two too many
for a line that must land in a single breath.
The phone wins: switched to airplane mode, it has already seen
more of the world this year than its owner has. One object, one
turn, plain words anyone would say out loud, and the envy hiding
inside the comparison is what makes it funny rather than cute.
"""

import os
from pathlib import Path

LAUGH_LINE = (
    "I put my phone on airplane mode, and it has already seen more "
    "of the world this year than I have."
)

LAUGH_CAP = 140


def laugh_fits(text: str) -> bool:
    # One breath is the unit of measurement here, so the check
    # counts characters and forbids the line a breath cannot hold.
    return 1 <= len(text) <= LAUGH_CAP and "\n" not in text and text == text.strip()


def tell_it() -> None:
    if not laugh_fits(LAUGH_LINE):
        raise SystemExit("laugh line outside the gate")
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(LAUGH_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    tell_it()

# Frequent-flyer note: the phone has requested a window seat
# for its next trip and, frankly, it has earned one.
