def contains_special_characters(text):
    for char in text:
        if not char.isalnum() and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    sample_string_1 = "Hello World 123"
    sample_string_2 = "Hello! World@ 123#"
    result_1 = contains_special_characters(sample_string_1)
    result_2 = contains_special_characters(sample_string_2)
    print(result_1)
    print(result_2)