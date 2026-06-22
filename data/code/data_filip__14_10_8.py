def has_unique_characters(text):
    return len(text) == len(set(text))
if __name__ == '__main__':
    test_cases = ['abcdefg', 'hello', 'world', 'python', 'aabbc', '', 'a', 'abca', '12345', '112233']
    for test_case in test_cases:
        result = has_unique_characters(test_case)
        print(f"String: '{test_case}', Unique Characters: {result}")