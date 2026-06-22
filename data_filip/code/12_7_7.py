def remove_formatting_and_validate(s):
    translation_table = str.maketrans('', '', ' \t\n\r,;.:!?"\'()-_+*/%&=<>[]{}|\\')
    cleaned = s.translate(translation_table)
    if cleaned == '':
        return False
    return cleaned.isdigit()

if __name__ == '__main__':
    test_string_1 = "123,456"
    test_string_2 = "abc-123"
    test_string_3 = "789"
    result_1 = remove_formatting_and_validate(test_string_1)
    result_2 = remove_formatting_and_validate(test_string_2)
    result_3 = remove_formatting_and_validate(test_string_3)
    print(result_1)
    print(result_2)
    print(result_3)