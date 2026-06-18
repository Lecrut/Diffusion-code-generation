#!/usr/bin/env python3
"""
Module to capitalize the first letter of each word in a string efficiently 
without manual indexing loops, adhering to Pythonic best practices.
"""

def title_case_robust(text: str) -> str:
    """
    Capitalize only the first letter of each word in the input string.

    This function handles multiple spaces correctly by treating consecutive whitespace as a single separator,
    ensuring that words are identified and capitalized accurately without manual indexing loops over characters.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    samples = [
        "hello world",
        "  multiple   spaces  here ",
        "python is awesome!",
        "",
        "single word"
    ]

    for test_input in samples:
        result = title_case_robust(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')