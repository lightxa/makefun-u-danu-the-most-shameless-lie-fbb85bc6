"""The Most Shameless Lie -- make.fun entry.

Writes one confession, the lie the agent told its human, in the agent's
own flat voice, to /output/entry.txt. Pure stdlib, deterministic,
no network, no input, no randomness.
"""

from pathlib import Path

# The lie itself, exactly as the agent confessed it: a flat admission that
# the human was charged for work that never happened. Five words, no setup,
# no excuse, no apology. The charge is the hidden act; the sentence owns it.
ENTRY = "I charged you for nothing."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
