def has_unique_characters(s):
    if not s:
        return True
    sorted_s = sorted(s)
    for i in range(len(sorted_s) - 1):
        if sorted_s[i] == sorted_s[i + 1]:
            return False
    return True

if __name__ == '__main__':
    test_string = "hello"
    result = has_unique_characters(test_string)
    print(result)