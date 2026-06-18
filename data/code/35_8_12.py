def count_vowels(text: str) -> int:
    """
    Counts the number of vowels in a string, ignoring non-alphabetic characters.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowel occurrences ('a', 'e', 'i', 'o', 'u' case-insensitive).
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to test the logic without user input or external dependencies.
    samples = [
        "Hello, World!",      # Expected: 2 (e, o)
        "AEIOUaeiou",         # Expected: 10
        "Rhythm is fun.",     # Expected: 3 (i, u) - 'y' is not counted here per strict vowel definition.
        "No vowels in this!", # Expected: 0
    ]

    for sample_text in samples:
        result = count_vowels(sample_text)
        print(f"Input: '{sample_text}' -> Vowel Count: {result}")