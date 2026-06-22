def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_strings = ["abcde", "hello", "", "a", "abcdea"]
    for s in test_strings:
        result = has_unique_characters(s)
        print(f"has_unique_characters('{s}') = {result}")