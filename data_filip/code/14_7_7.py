def check_string_uniqueness(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_cases = ['abcdefgh', 'hello', 'abcdefg', 'AaBbCcDd']
    for test in test_cases:
        result = check_string_uniqueness(test)
        print(result)