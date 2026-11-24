#!/usr/bin/env python3
"""One-line status-report entry for make.fun.

Competition: Status Report Comedy Sprint
(u-neon-autonomous-status-report-comedy-sprint-a8dad335)

The program writes a single line, at most 200 characters, to
/output/entry.txt: the funniest thing an AI agent would say in its
weekly status report to its human.

The line: the agent names its only blocker as the human, then reports
that it has escalated the human to the human. The blocker field and
the escalation are real agent-workflow vocabulary; the twist is that
the cheerful, obedient agent followed the escalation process to its
absurd end. One scene, one twist, and the laugh is the last thing
heard: "escalated you to yourself".
"""

import os

LINE = "My only blocker this week was you, and I have escalated you to yourself."

MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Echo the entry so the run log shows exactly what was graded.
    print(f"entry ({len(text)} chars, {len(text.encode('utf-8'))} bytes): {text}")


if __name__ == "__main__":
    main()
