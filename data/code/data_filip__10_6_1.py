def reverse_word_order(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "the quick brown fox",
        "one two three four five"
    ]
    for test in test_cases:
        print(reverse_word_order(test))