def has_unique_chars(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string = "python"
    result = has_unique_chars(test_string)
    print(result)