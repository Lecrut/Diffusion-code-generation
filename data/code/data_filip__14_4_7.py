def has_duplicate_chars(s):
    return len(s) != len(set(s))

if __name__ == '__main__':
    test_string = "hello"
    result = has_duplicate_chars(test_string)
    print(result)