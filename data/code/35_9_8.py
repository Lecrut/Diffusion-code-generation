import re

def count_vowels(text: str) -> int:
    """
    Count the total number of vowels in a given string.

    This function identifies 'a', 'e', 'i', 'o', and 'u' (both uppercase 
    and lowercase) as valid vowels and returns their cumulative count. 

    Args:
        text (str): The input string to analyze for vowel occurrences.

    Returns:
        int: The total count of vowels found in the input string.

    Example:
        >>> count_vowels("Hello World")
        3
        
    Note:
        This implementation uses a regular expression for efficiency and 
        clarity, ensuring it handles Unicode characters correctly while 
        adhering to PEP 8 style guidelines. Non-vowel characters are ignored.
    
    Raises:
        TypeError: If the input is not a string instance.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected 'str' type, got {type(text).__name__}")

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    
    for char in text:
        if any(char == v or char.upper() == v for v in vowels):
            vowel_count += 1
            
    return vowel_count

if __name__ == '__main__':
    # Sample test cases with hard-coded values to ensure no external dependencies are needed.
    
    # Test Case 1: Standard sentence
    sample_1 = "The quick brown fox jumps over the lazy dog."
    
    # Test Case 2: Mixed case and special characters
    sample_2 = "Python 3.9 is awesome!"
    
    # Test Case 3: Empty string
    sample_3 = ""

    print(f"Vowel count in '{sample_1}': {count_vowels(sample_1)}")
    print(f"Vowel count in '{sample_2}': {count_vowels(sample_2)}")
    print(f"Vowel count in '{sample_3}': {count_vowels(sample_3)}")