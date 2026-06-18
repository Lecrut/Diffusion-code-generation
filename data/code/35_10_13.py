def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a given string.
    The check is case-insensitive.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The count of vowel characters found.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert the text to lowercase for case-insensitive comparison and iterate through each character
    return sum(1 for char in text.lower() if char in vowels_set)

if __name__ == '__main__':
    # Sample test cases run without user input, command-line arguments, or network access.
    
    sample_1 = "Hello World!"
    expected_1 = 2
    
    sample_2 = "AEIOUaeiou"
    expected_2 = 10
    
    sample_3 = "Python Programming Language"
    expected_3 = 7

    # Verify results against expectations for robustness checks.
    
    result_1 = count_vowels(sample_1)
    assert result_1 == expected_1, f"Test failed: Expected {expected_1}, got {result_1}"
    
    result_2 = count_vowels(sample_2)
    assert result_2 == expected_2, f"Test failed: Expected {expected_2}, got {result_2}"
    
    result_3 = count_vowels(sample_3)
    assert result_3 == expected_3, f"Test failed: Expected {expected_3}, got {result_3}"

    print("All sample tests passed successfully.")