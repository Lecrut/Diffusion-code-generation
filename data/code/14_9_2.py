def all_unique_characters(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string_1 = "abcdefg"
    test_string_2 = "hello"
    print(all_unique_characters(test_string_1))
    print(all_unique_characters(test_string_2))