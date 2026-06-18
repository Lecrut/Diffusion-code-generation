import string

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given string.

    This function considers 'a', 'e', 'i', 'o', and 'u' as vowels,
    regardless of whether they are uppercase or lowercase. It ignores
    any other characters present in the input text.

    Args:
        text (str): The input string to analyze for vowel count.

    Returns:
        int: The total number of vowels found in the input string.

    Examples:
        >>> count_vowels("Hello")  # e, o are vowels -> returns 2
        >>> count_vowels("")         # empty string -> returns 0
        >>> count_vowels("AEIOU")   # all uppercase vowels -> returns 5
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected a string input, got {type(text).__name__}")

    vowel_set = set(string.ascii_letters) & {"aeiouAEIOU"}
    
    count = sum(1 for char in text.lower() if char in "aeiou")

    return count

if __name__ == '__main__':
    pass
