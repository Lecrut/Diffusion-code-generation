def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string, case-insensitive.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found in the string.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "aeiouAEIOU",
        "xyz"
    ]

    for text in test_cases:
        count = count_vowels(text)
        print(f"'{text}' -> {count} vowels")