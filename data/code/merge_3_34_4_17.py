#!/usr/bin/env python3
"""
Command-line utility to capitalize the first letter of each word in input text.

This script reads a sample string directly, processes it by capitalizing 
the first character of every word while preserving case for subsequent characters,
and prints the result without any interactive prompts or argument parsing.
"""

def title_case(text: str) -> str:
    """Return text with only the first letter of each word capitalized."""
    # Split into words (default splits on whitespace), capitalize each, then join back.
    return " ".join(word.capitalize() for word in text.split()) if text else ""

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or external dependencies.
    samples = [
        "hello world",
        "python is fun!",
        "  multi   line     support  ",
        "",
        "a b c d e f g h i j k l m n o p q r s t"
    ]

    for sample in samples:
        result = title_case(sample)
        print(result)