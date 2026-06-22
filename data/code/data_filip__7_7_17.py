def contains_special_characters(s: str) -> bool:
    if not s:
        return False
    original_length = len(s)
    stripped_length = len(''.join(c for c in s if c.isalnum()))
    return original_length != stripped_length

if __name__ == '__main__':
    test_string_1 = "HelloWorld"
    test_string_2 = "Hello@World"
    test_string_3 = "12345"
    test_string_4 = "123@45"
    result_1 = contains_special_characters(test_string_1)
    result_2 = contains_special_characters(test_string_2)
    result_3 = contains_special_characters(test_string_3)
    result_4 = contains_special_characters(test_string_4)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)