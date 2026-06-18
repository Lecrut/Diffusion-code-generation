import sys

def count_vowels(word: str) -> int:
    """Count total vowels in a given word."""
    if not isinstance(word, str):
        return 0
    
    # Define set of vowels (both lowercase and uppercase for optimization checks)
    vowels = {'a', 'e', 'i', 'o', 'u'} | {'A', 'E', 'I', 'O', 'U'}
    
    count = 0
    word_lower = word.lower()
    return sum(1 if char in vowels else 0 for char in word_lower)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    test_cases = [
        "hello",
        "beautiful day",
        "",
        "AEIOUaeiou"
    ]

    for word in test_cases:
        vowel_count = count_vowels(word)
        print(f"The total vowel count is {vowel_count}")