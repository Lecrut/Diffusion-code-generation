def count_vowels(text: str) -> int:
    """Count vowels (a, e, i, o, u) in a string, case-insensitive."""
    return sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == '__main__':
    sample_strings = ["Hello", "HELLO WORLD!", "Python 3.9", ""]
    
    print("Vowel counts:")
    for s in sample_strings:
        count = count_vowels(s)
        print(f"String '{s}': {count}")