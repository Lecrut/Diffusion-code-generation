"""Vowel counter module providing a reusable function to count vowels in text."""

def count_vowels(text: str) -> int:
    """Count the number of vowel characters ('a', 'e', 'i', 'o', 'u') in the given string.

    The counting is case-insensitive and includes both uppercase and lowercase vowels.
    Other unicode letters that might be considered vowels by certain languages are not included,
    adhering to a simple ASCII-based definition unless extended otherwise.

    Args:
        text (str): The input string in which vowel characters will be counted.

    Returns:
        int: The total count of vowel characters found in the input string.

    Examples:
        >>> count_vowels("Hello World")
        2
        >>> count_vowels("AEIOUaeiou123!")
        9
        
    Raises:
        TypeError: If the input is not a string type.
    
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string type, got {type(text).__name__}")

    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    
    for char in text:
        if char.lower() in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    sample_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Hello World!",
        "",
        "AEIOU",  # All uppercase vowels
        "xyzabc1234567890"  # No vowels
    ]

    for test_string in sample_texts:
        result = count_vowels(test_string)
        print(f"'{test_string}' contains {result} vowel(s).")