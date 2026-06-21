def has_all_unique_characters(s: str) -> bool:
    seen_characters = set()
    for char in s:
        if char in seen_characters:
            return False
        seen_characters.add(char)
    return True

if __name__ == '__main__':
    test_string = "programming"
    result = has_all_unique_characters(test_string)
    print(result)
    test_string_2 = "abcdef"
    result_2 = has_all_unique_characters(test_string_2)
    print(result_2)