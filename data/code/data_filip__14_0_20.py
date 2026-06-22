def has_unique_chars(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string = "abcdef"
    result = has_unique_chars(test_string)
    print(result)