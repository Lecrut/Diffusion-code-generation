def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_strings = ["abcdef", "hello", "world", ""]
    for text in test_strings:
        print(has_unique_characters(text))