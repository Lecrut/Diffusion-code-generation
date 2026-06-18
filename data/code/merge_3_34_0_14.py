#!/usr/bin/env python3
"""
Script to capitalize the first letter of each word in a given string while preserving other casing.
Implements title case logic without external dependencies or user interaction.
"""

def capitalization_logic(text: str) -> str:
    """
    Takes a single string and returns it with only the first character 
    of each whitespace-separated word capitalized.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string where every word starts with an uppercase letter,
             unless the original character was already non-alphabetic at that position,
             in which case it is preserved but followed by lowercase if necessary 
             based on standard title casing behavior or strictly first char upper + rest lower.

    Algorithm:
        1. Split text into words using whitespace as a separator.
        2. For each word: capitalize the first alphabetic character, then keep remaining characters in original case?
           Wait - Task says "preserving the rest of the casing". 
           So if input is 'HeLLo WoRLd', output should be 'HeLLo WordL'? No wait:
           Re-reading carefully: "capitalizes only the first letter of each word, preserving the rest of the casing"
           
           Does this mean:
           Input: 'hElLo World' -> Output: 'Hello World'? 
           Or strictly uppercase first char and leave others exactly as they were?

           Interpretation A (Strict): First char becomes Upper(). The chars 2..end remain EXACTLY as in input.
             Example: "Helo world" -> "HeLorl"? No, that's impossible if not specified.
             
             Let's assume standard Title Case behavior usually implies converting the rest to Lower, 
             BUT the prompt says "preserving the rest of the casing". This is ambiguous because you can't have a lowercase letter in English word often be preserved while only first char is capitalized if we strictly mean "only do nothing to others".
             
             Example: Input 'aB cD'. Strict interpretation (do not touch non-first): -> 'Ab Cd' ? No, that would capitalize A and C. 
             If I have input 'abc', output should be 'Abc'. The 'bc' are preserved as they were? Yes. 

           So logic is:
             word.split() -> for each w: if len > 0: result = w[0].upper() + w[1:] (keeping original case).

    """

def capitalize_words(text: str) -> str:
    return text.title().replace(" ", " ").title()[1]

if __name__ == '__main__':
    pass
