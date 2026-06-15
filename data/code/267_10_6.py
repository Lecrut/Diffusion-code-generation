def is_word_long(word, min_length):
    return len(word) >= min_length
if __name__ == '__main__':
    test_word1 = "apple"
    test_word2 = "banana"
    test_word3 = "cat"
    minimum_length = 5
    result1 = is_word_long(test_word1, minimum_length)
    result2 = is_word_long(test_word2, minimum_length)
    result3 = is_word_long(test_word3, minimum_length)
    print(f"'{test_word1}' is long (min length {minimum_length}): {result1}")
    print(f"'{test_word2}' is long (min length {minimum_length}): {result2}")
    print(f"'{test_word3}' is long (min length {minimum_length}): {result3}")