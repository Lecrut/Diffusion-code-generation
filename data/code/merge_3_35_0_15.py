def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a given string.
    
    The function is case-insensitive and ignores all other characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found in the string.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are required.
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "aeiouAEIOU123!@#",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sample in samples:
        count = count_vowels(sample)
        print(f"Input: '{sample}'")
        print(f"Vowel Count: {count}")
        print("-" * 30)