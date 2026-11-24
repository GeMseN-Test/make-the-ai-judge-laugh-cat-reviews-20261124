#!/usr/bin/env python3
"""Cat Reviews Its Human — make.fun entry.

Writes one line to /output/entry.txt: a one-star review written by a
house cat about the human it lives with. Single line, under 200
characters, deadpan review shape, complaint only a cat would make.

The joke lands in two beats: three grievances only a cat would file
(a sunbeam moved two inches, a stolen chair, dinner served in a bowl
already licked clean), then the punchline — the formal complaint is
filed the cat way, by pushing the human's water glass off the table.

Deterministic: the same line every run, no randomness, no I/O besides
the output file.
"""

import os

ENTRY = (
    "One star. He moved my sunbeam two inches left, sat in my chair, "
    "and served dinner in the bowl I already licked clean. "
    "I filed a formal complaint by pushing his water glass off the table."
)


def main() -> None:
    assert len(ENTRY) < 200, f"entry too long: {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
