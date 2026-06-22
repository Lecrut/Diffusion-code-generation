def is_unique(s):
    sorted_chars = sorted(s)
    for i in range(1, len(sorted_chars)):
        if sorted_chars[i] == sorted_chars[i - 1]:
            return False
    return True

if __name__ == '__main__':
    test_string = "abcdef"
    result = is_unique(test_string)
    print(result)