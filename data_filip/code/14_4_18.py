def has_duplicates(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    test_strings = ['abcdef', 'hello', 'python', 'programming']
    for test in test_strings:
        result = has_duplicates(test)
        print(f"{test}: {result}")