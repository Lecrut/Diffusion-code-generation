def reverse_words(sentence):
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")
    n = len(sentence)
    result_words = []
    start = 0
    i = 0
    while i < n:
        if sentence[i] == ' ':
            if start < i:
                word = sentence[start:i]
                result_words.insert(0, word)
            start = i + 1
        i += 1
    if start < n:
        word = sentence[start:n]
        result_words.insert(0, word)
    return ' '.join(result_words)

if __name__ == '__main__':
    test_case_1 = "Python is great"
    test_case_2 = "  multiple   spaces  "
    test_case_3 = "SingleWord"
    print(reverse_words(test_case_1))
    print(reverse_words(test_case_2))
    print(reverse_words(test_case_3))