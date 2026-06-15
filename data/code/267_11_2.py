def is_word_long(word: str, threshold: int) -> bool:
    return len(word) > threshold
if __name__ == '__main__':
    test_word1 = "short"
    test_threshold1 = 5
    result1 = is_word_long(test_word1, test_threshold1)
    print(f"{test_word1} > {test_threshold1}: {result1}")
    test_word2 = "longerword"
    test_threshold2 = 7
    result2 = is_word_long(test_word2, test_threshold2)
    print(f"{test_word2} > {test_threshold2}: {result2}")
    test_word3 = "test"
    test_threshold3 = 4
    result3 = is_word_long(test_word3, test_threshold3)
    print(f"{test_word3} > {test_threshold3}: {result3}")