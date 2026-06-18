#!/usr/bin/env python3
"""Script to calculate and print the length of a phrase."""

def get_phrase_length(phrase: str) -> int:
    """Return the exact length of the provided phrase string."""
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, sys.stdin, argparse required arguments, or network access is used here.
    phrases = ["Hello", "Python Programming"]

    for phrase in phrases:
        length = get_phrase_length(phrase)
        print(length)