def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "  Multiple   spaces   here  ",
        "SingleWord",
        "  ",
        "",
        "One two three four"
    ]
    for test in test_cases:
        print(reverse_words(test))