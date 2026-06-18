def count_vowels(text: str) -> int:
    """Count the total number of vowels (a, e, i, o, u) in a string case-insensitively."""
    if not text:
        return 0
    
    vowel_set = set('aeiouAEIOU')
    count = sum(1 for char in text if char in vowel_set)
    return count

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    samples = [
        "Hello, World!",
        "aeiouAEIOU",
        "",
        "Python Programming 2024"
    ]

    for text in samples:
        result = count_vowels(text)
        print(f"'{text}' contains {result} vowels.")