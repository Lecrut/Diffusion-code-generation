def has_unique_chars(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "abcdefg"
    print(has_unique_chars(test_string))
    test_string_duplicate = "hello"
    print(has_unique_chars(test_string_duplicate))