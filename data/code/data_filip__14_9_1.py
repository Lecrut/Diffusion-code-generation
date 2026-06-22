def has_unique_chars(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "abcdefg"
    result = has_unique_chars(test_string)
    print(result)