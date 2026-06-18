def reverse_word(word):
    """Returns the reversed version of the given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive prompts or input() calls
    sample_words = ["hello", "world"]
    
    for test_case in sample_words:
        result = reverse_word(test_case)
        print(f"Original word: {test_case}")
        print("Reversed word:", result)