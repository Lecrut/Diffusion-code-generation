def is_word_long(word, min_length):
    return len(word) >= min_length
if __name__ == '__main__':
    test_word_1 = "programming"
    test_word_2 = "short"
    test_word_3 = "medium"
    minimum_length = 6
    result_1 = is_word_long(test_word_1, minimum_length)
    result_2 = is_word_long(test_word_2, minimum_length)
    result_3 = is_word_long(test_word_3, minimum_length)
    print(f"Is '{test_word_1}' long (min length {minimum_length}): {result_1}")
    print(f"Is '{test_word_2}' long (min length {minimum_length}): {result_2}")
    print(f"Is '{test_word_3}' long (min length {minimum_length}): {result_3}")