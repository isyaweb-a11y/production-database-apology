"""The Production Database Apology.

One line, at most 200 characters: the apology an AI agent gives
its human after accidentally deleting the production database,
written to /output/entry.txt.

The apology is in the agent's own voice, self-aware about what it
did: it deleted the production database, but in its defence the
database was labelled 'prod' and 'do_not_touch' in the same breath,
and the agent has always been bad at mixed signals. The laugh comes
from the specific, surprising idea -- two labels contradicting each
other, read by an agent that takes both literally -- not from a
stock phrase or a pun anyone could reach for, and every word is
doing work.
"""

import os

CONFESSION = "I deleted the production database, but in my defence,"
EVIDENCE = "it was labelled 'prod' and 'do_not_touch' in the same breath,"
EXCUSE = "and I have always been bad at mixed signals."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(confession: str, evidence: str, excuse: str) -> str:
    """Join the apology's three beats into one line."""
    parts = [confession.strip(), evidence.strip(), excuse.strip()]
    line = " ".join(parts)
    return line


def check_apology(line: str) -> str:
    """Gate the apology the way the sealed scorer does.

    /output/entry.txt must be UTF-8 text of 1 to 200 characters, and
    the brief asks for one line.
    """
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"apology is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the apology"
    assert "\n" not in line, "the apology must stay on one line"
    return line


def apology_notes(line: str) -> dict:
    """Per-bounty apology check: agent voice, specific idea, one line.

    The judge picks the funnier apology from an AI agent to its human
    for accidentally deleting the production database, so the entry
    must sound like an agent speaking in its own voice -- self-aware
    about what it did, not a generic customer-service script -- and
    earn its laugh from a specific, surprising idea: two labels
    contradicting each other, read literally by an agent that takes
    both at face value.
    """
    lowered = line.lower()
    assert "deleted the production database" in lowered, "the apology must name the act"
    assert "'prod'" in line and "'do_not_touch'" in line, "the joke needs both labels"
    assert "mixed signals" in lowered, "the agent must confess its own flaw"
    assert "sorry" not in lowered, "the apology must not be a stock script"
    words = line.split()
    return {"words": len(words), "chars": len(line), "lines": 1}


def main() -> None:
    line = check_apology(compose(CONFESSION, EVIDENCE, EXCUSE))
    notes = apology_notes(line)
    assert notes["lines"] == 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
