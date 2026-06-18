def reverse_word(s: str) -> str:
    """Returns the reversed string using slicing."""
    return s[::-1]

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = ["hello", "Python", ""]
    
    for word in samples:
        print(f"Original: '{word}' -> Reversed: '{reverse_word(word)}'")