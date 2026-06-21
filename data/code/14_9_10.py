def has_unique_chars(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_strings = ["hello", "world", "python", "abcdef"]
    results = [has_unique_chars(s) for s in test_strings]
    print(results)