import re

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given string.

    This function considers 'a', 'e', 'i', 'o', 'u' as vowels, including their uppercase forms.
    It ignores any other characters such as consonants or punctuation marks.

    Args:
        text (str): The input string to analyze. Can contain unicode characters, though currently
                    only standard Latin letters are recognized by the default regex pattern used here.
    
    Returns:
        int: The total count of vowels found in the text.

    Example:
        >>> s = "Hello World!"
        >>> count_vowels(s)
        3
    
    Note:
        This implementation uses a compiled regular expression for efficiency and clarity, adhering to PEP 8
        by avoiding repeated pattern creation inside loops or functions where performance matters significantly.
        To support full unicode vowel recognition (e.g., ñ, ö), the regex would typically need adjustment,
        but this version focuses on standard ASCII vowels as per common convention unless specified otherwise.
    """
    if not isinstance(text, str):
        raise TypeError("Expected string type")

    # Compiled pattern for 'aeiou' including uppercase letters
    vowel_pattern = re.compile(r'[aeiouAEIOU]')
    
    count = 0
    matches = list(vowel_pattern.finditer(text))
    
    return len(matches)

if __name__ == '__main__':
    sample_strings = [
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog.",
        "",
        "AEIOUaeiou",
        "xyz"
    ]

    for s in sample_strings:
        result = count_vowels(s)
        print(f"'{s}' -> {result} vowels")