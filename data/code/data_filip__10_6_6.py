def reverse_word_order(text):
    return ' '.join(text.split()[::-1])

if __name__ == '__main__':
    test_cases = [
        "The quick brown fox",
        "Hello world this is a test",
        "Python is great"
    ]
    for case in test_cases:
        print(reverse_word_order(case))