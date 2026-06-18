import string

def count_vowels(text: str) -> int:
    """
    Count the number of vowels in a given string.

    This function considers both uppercase and lowercase vowels ('a', 'e', 'i', 'o', 'u').
    Non-alphabetic characters are ignored without raising errors for invalid input types,
    as long as they can be converted to strings (which all Python objects support).

    Args:
        text (str): The string in which vowels are to be counted.

    Returns:
        int: The count of vowel occurrences in the provided string.

    Examples:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("")
        0
    
    Raises:
        TypeError: If `text` is not a string instance (though typically this function handles strings only).
    
    Note:
        This implementation follows PEP 8 style guidelines, including snake_case for functions and
        clear separation of logic from main execution flow. No interactive input or external dependencies are used.

    """
    vowels = set(string.ascii_lowercase + string.ascii_uppercase) & {'aeiou'} # Ensure case-insensitive check via membership test
    
    count = 0
    for char in text:
        if char.lower() in 'aeiou':
            count += 1
            
    return count

if __name__ == '__main__':
    sample_text_1 = "Hello, World! This is a comprehensive example."
    sample_text_2 = ""
    
    result_1 = count_vowels(sample_text_1)
    result_2 = count_vowels(sample_text_2)
    
    print(f"Vowel count in '{sample_text_1}': {result_1}")
    print(f"Vowel count in empty string: {result_2}")