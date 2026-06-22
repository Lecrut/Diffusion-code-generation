def is_unique_chars(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string = "abcdefg"
    result = is_unique_chars(test_string)
    print(result)
    test_string_duplicate = "hello"
    result_duplicate = is_unique_chars(test_string_duplicate)
    print(result_duplicate)