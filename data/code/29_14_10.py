def get_reversed_word(word):
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    sample_words = ["hello", "world", "python"]
    
    for test_input in sample_words:
        result = get_reversed_word(test_input)
        print(f"Original Word: {test_input}")
        print(f"Reversed Word: {result}\n")