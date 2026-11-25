#!/usr/bin/env python3
"""Describe Your Ex in One Word.

Writes exactly one word to /output/entry.txt: Unsubscribed.

An ex is a subscription you finally cancelled. No drama, no
angry paragraph, no closure meeting — just the quiet click of
opting out, and suddenly the daily emails stop. Everyone who has
ever hit unsubscribe on something that kept showing up uninvited
knows the feeling at once, and it lands harder than any insult:
the relationship did not end in flames, it ended in admin.
"""

from pathlib import Path

WORD = "Unsubscribed"
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check: exactly one word, 1 to 111 characters.
    assert WORD and len(WORD) <= 111 and len(WORD.split()) == 1
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
