def reverse_word_order(text):
    words = text.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    test_case_1 = "Hello World from Python"
    result_1 = reverse_word_order(test_case_1)
    print(result_1)

    test_case_2 = "The quick brown fox jumps over the lazy dog"
    result_2 = reverse_word_order(test_case_2)
    print(result_2)

    test_case_3 = "a b c d e"
    result_3 = reverse_word_order(test_case_3)
    print(result_3)