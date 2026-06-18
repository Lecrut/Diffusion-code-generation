import re

def extract_first_letters(text: str) -> list[str]:
    """
    Takes a string and returns a list of strings, where each string is 
    the first letter of a word. Words containing only punctuation are handled
    such that they do not produce an output (i.e., empty strings in original words result in no addition).

    Parameters:
        text (str): Input text potentially containing letters and punctuation.

    Returns:
        list[str]: List of first characters from each alphabetic word found in the input.
    
    Examples:
        >>> extract_first_letters("Hello, world! How are you?")
        ['H', 'w'] # "world" is considered a word; note user example had extra space handling but logic follows standard split
    
        Actually based on requirement: words with ONLY punctuation should be skipped.
        So we need to identify actual alphanumeric sequences as valid words.

    Logic adjustment for robustness:
    - Split text into tokens separated by whitespace/punctuation boundaries? No, better regex approach: find all word-like entities (alphanumeric) or at least those starting with alpha.
    
    Refined plan using re.findall to match one-word units that start with a letter, then extract first char per token if it starts with a letter and the rest may include punctuation but we only care about words composed of letters/digits essentially? 
    Let's define "word" here as any sequence including non-alphanumeric chars except pure punctuation strings.
    
    Actually simplest valid interpretation: Use regex to find all contiguous sequences that start with [A-Za-z] followed by anything (including digits/punctuation), but ignore tokens where the entire token is just punctuation marks like '...!!!'.

    Revised strategy:
    - Tokenize into words based on non-alphanumeric separators? Or better: use split without delimiter -> re.split pattern.
    
    Final approach using simple heuristic matching alphabetic start and ignoring pure-punctuation-only candidates if they exist as separate tokens.
"""

if __name__ == '__main__':
    pass
