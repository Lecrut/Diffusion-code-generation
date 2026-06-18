def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a given string.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels found in the string.
    """
    vowel_set = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowel_set)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "aeiouAEIOU",
        "",
        "xyz"
    ]

    for text in test_cases:
        count = count_vowels(text)
        print(f"'{text}' contains {count} vowel(s).")