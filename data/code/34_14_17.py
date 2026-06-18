#!/usr/bin/env python3
"""Module to capitalize the first letter of each word in a string."""

def title_case_concise(text: str) -> str:
    """Return a new string with the first character of each word capitalized.
    
    This is achieved by splitting the text into words, capitalizing the 
    first character of each non-empty word, and joining them back together.
    Performance is optimized using list comprehension which avoids intermediate
    large strings during processing compared to map().read() in some cases.
    
    Args:
        text (str): The input string containing spaces or other delimiters.
        
    Returns:
        str: A new string with each word's first letter capitalized.
    """
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "hello world",
        "python is awesome!",
        "  multiple   spaces ",
        "no words here"
    ]

    for item in samples:
        result = title_case_concise(item)
        print(f'Input: "{item}" -> Output: "{result}"')