def has_special_characters(text):
    for char in text:
        if not char.isalnum() and char != ' ':
            return True
    return False

if __name__ == '__main__':
    sample_string_1 = "Hello World 123"
    sample_string_2 = "Hello@World!"
    sample_string_3 = "NormalString123"
    sample_string_4 = "Has Special Char $"

    print(has_special_characters(sample_string_1))
    print(has_special_characters(sample_string_2))
    print(has_special_characters(sample_string_3))
    print(has_special_characters(sample_string_4))