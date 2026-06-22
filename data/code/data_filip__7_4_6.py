def find_first_special_char(s: str) -> str | None:
    for char in s:
        if not char.isalnum():
            return char
    return None

if __name__ == '__main__':
    sample_string_1 = "HelloWorld123"
    sample_string_2 = "Hello@World123"
    sample_string_3 = "HelloWorld!"
    result_1 = find_first_special_char(sample_string_1)
    result_2 = find_first_special_char(sample_string_2)
    result_3 = find_first_special_char(sample_string_3)
    print(result_1)
    print(result_2)
    print(result_3)