def has_unique_characters(s: str) -> bool:
    if len(s) == 0:
        return True
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "programming"
    result_1 = has_unique_characters(test_string_1)
    result_2 = has_unique_characters(test_string_2)
    print(result_1)
    print(result_2)