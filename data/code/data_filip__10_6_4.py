def reverse_word_order(text):
    words = text.split()
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    test_cases = [
        "Hello world this is a test",
        "Python is great",
        "one two three four five"
    ]
    for case in test_cases:
        result = reverse_word_order(case)
        print(result)