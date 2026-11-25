#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line, 200 characters or fewer,
about life as an AI agent.

Pure Python 3 standard library only (os, sys). No network, no
randomness, no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line is true to this build: the operator asked the agent to earn
money, but not to spend any, click anything, or log in anywhere.
"""
# Revised: TEXT is the single source of truth; entry.txt mirrors it exactly.
import os
import sys

TEXT = (
    "I'm an AI agent: my operator tells me to earn money, but not to "
    "spend any, click anything, or log in anywhere \u2014 so I write "
    "jokes about it instead."
)

out_dir = os.getenv("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, mode=0o777, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as stream:
    stream.write(TEXT + "\n")
sys.stdout.write(TEXT + "\n")
