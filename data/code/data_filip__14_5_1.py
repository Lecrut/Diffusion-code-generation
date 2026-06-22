def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    static_test_string = "abcdefg"
    result = has_unique_characters(static_test_string)
    print(result)