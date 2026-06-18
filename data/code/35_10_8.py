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

    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "aeiouAEIOU",
        "xyz"
    ]

    for text in test_cases:
        count = count_vowels(text)
        print(f"'{text}' contains {count} vowel(s).")