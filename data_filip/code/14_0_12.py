def is_unique_chars(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string = "abcdefg123!@#"
    result = is_unique_chars(test_string)
    print(result)