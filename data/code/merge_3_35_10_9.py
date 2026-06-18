def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string, case-insensitive.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "aeiouAEIOU"
    ]

    for test_string in samples:
        count = count_vowels(test_string)
        print(f"'{test_string}' -> {count} vowels")