def is_word_long(word, min_length):
    return len(word) >= min_length
if __name__ == '__main__':
    test_word1 = "programming"
    test_word2 = "short"
    test_word3 = "medium"
    minimum_length = 7
    result1 = is_word_long(test_word1, minimum_length)
    result2 = is_word_long(test_word2, minimum_length)
    result3 = is_word_long(test_word3, minimum_length)
    print(f"Is '{test_word1}' long (min length {minimum_length}): {result1}")
    print(f"Is '{test_word2}' long (min length {minimum_length}): {result2}")
    print(f"Is '{test_word3}' long (min length {minimum_length}): {result3}")