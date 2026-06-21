def has_unique_characters(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string = "abcdefg"
    result = has_unique_characters(test_string)
    print(result)