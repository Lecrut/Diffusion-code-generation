def reverse_word(word: str) -> str:
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    sample_words = ["hello", "world", "Python"]
    
    for test_case in sample_words:
        original = reverse_word(test_case)
        print(f"Original: {test_case}")
        print(f"Reversed: {original}\n")