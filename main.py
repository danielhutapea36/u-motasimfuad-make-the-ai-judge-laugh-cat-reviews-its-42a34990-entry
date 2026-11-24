#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes a single one-star review, written by a house cat about the
human it lives with, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). The line is 115 characters, UTF-8, one line, no trailing
newline. Deterministic: no randomness, no network, no time
dependence — every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a funny one-star
review written by a house cat about its human, (2) a specific and
recognisable complaint — here the laptop keyboard, one of the
brief's own examples, (3) a voice unmistakably feline: the human
is measured by cat standards, and the review gives away more
about the cat than the owner, (4) a turn in the last few words
that rewards a second read, (5) the deadpan shape of a real
one-star review while the content goes somewhere absurd. The
complaint is concrete — lifted off the keyboard mid-sentence —
and the sting lands at the end: the cat wrote the review, the
human only typed it. The premise needs no explaining: a stranger
reading it cold gets the joke from the line alone. The deadpan
holds throughout — "One star.", the formal complaint, the
verdict — while the content itself is absurd: a cat filing a
review about being removed from its own keyboard.
"""

import os

TEXT = (
    "One star. He lifts me off the keyboard mid-sentence and calls "
    "it 'his work'. I wrote this review. He only typed it."
)


def main() -> None:
    # Gate: entry.txt must be 1–200 characters of UTF-8 text, not only
    # whitespace. The line is 115 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
