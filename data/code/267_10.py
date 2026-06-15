def is_word_long(word, min_length):
    return len(word) >= min_length
if __name__ == '__main__':
    test_word_1 = "short"
    test_word_2 = "longerword"
    min_len_1 = 5
    min_len_2 = 10
    result_1_1 = is_word_long(test_word_1, min_len_1)
    result_1_2 = is_word_long(test_word_2, min_len_1)
    result_2_1 = is_word_long(test_word_1, min_len_2)
    result_2_2 = is_word_long(test_word_2, min_len_2)
    print(f"Is '{test_word_1}' long (min length {min_len_1}): {result_1_1}")
    print(f"Is '{test_word_2}' long (min length {min_len_1}): {result_1_2}")
    print(f"Is '{test_word_1}' long (min length {min_len_2}): {result_2_1}")
    print(f"Is '{test_word_2}' long (min length {min_len_2}): {result_2_2}")