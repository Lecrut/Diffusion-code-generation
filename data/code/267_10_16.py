def is_word_long(word):
    if not isinstance(word, str):
        raise ValueError("Input must be a string.")
    return len(word) > 5

if __name__ == '__main__':
    test_word_1 = "short"
    test_word_2 = "longerword"
    result_1 = is_word_long(test_word_1)
    result_2 = is_word_long(test_word_2)
    print(f"Is '{test_word_1}' long: {result_1}")
    print(f"Is '{test_word_2}' long: {result_2}")