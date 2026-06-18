def reverse_word(word):
    """Reverses a given word."""
    return word[::-1]

if __name__ == '__main__':
    sample_words = ["hello", "world", "programming"]
    
    print("Running CLI reversal demonstration with hard-coded samples.")
    
    for test_input in sample_words:
        reversed_word = reverse_word(test_input)
        print(f"Original word: {test_input}")
        print(f"Reversed word:  {reversed_word}\n")