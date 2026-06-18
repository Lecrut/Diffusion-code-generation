import string

def count_vowels(text: str) -> int:
    """Returns the total number of vowels in the given text, case-insensitive."""
    if not isinstance(text, str):
        return 0
    vowel_count = sum(1 for char in text.lower() if char in 'aeiou')
    return vowel_count

if __name__ == '__main__':
    sample_words = ["hello", "sky", "rainbow"]
    
    # Simulate a prompt scenario without using interactive input functions as per constraints.
    # We iterate through hard-coded sample values to demonstrate the functionality.
    for word in sample_words:
        vowel_total = count_vowels(word)
        print(f"Word '{word}' contains {vowel_total} vowels.")