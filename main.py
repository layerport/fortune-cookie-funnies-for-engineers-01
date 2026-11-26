#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers -- make.fun bounty entry.

Writes one fortune-cookie message for a software engineer to
/output/entry.txt. Deterministic: the same bytes on every run.
Standard library only, so it runs in the grader's bare image.
"""

from pathlib import Path

# The fortune: a Heisenbug that only shows up when it matters most.
# Fortune-cookie declarative, engineer world (reproduce / manager),
# and the funniest word lands at the very end.
ENTRY = "The bug you cannot reproduce will reproduce itself in front of your manager."


def main() -> None:
    """Write the entry text to /output/entry.txt, exactly as-is."""
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    # No trailing newline: the file holds exactly the fortune, so the
    # gate counts the characters of the line itself and nothing else.
    target.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
