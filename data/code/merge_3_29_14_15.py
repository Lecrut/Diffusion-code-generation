def reverse_word(word: str) -> str:
    """Reverses a given word."""
    return word[::-1]

if __name__ == '__main__':
    sample_words = ["hello", "world", "Python"]
    
    for test_input in sample_words:
        reversed_output = reverse_word(test_input)
        print(f"Original: {test_input}")
        print(f"Reversed: {reversed_output}\n")