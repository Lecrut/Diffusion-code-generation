def sanitize_and_validate_integers(input_string):
    translation_table = str.maketrans('', '', ' \t\n\r\x0b\x0f,.-')
    cleaned_string = input_string.translate(translation_table)
    if not cleaned_string:
        return False
    try:
        int(cleaned_string)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    sample_value_1 = "12345"
    sample_value_2 = "12a34"
    sample_value_3 = "  987,654.321  "
    sample_value_4 = "no-ints-here"
    print(sanitize_and_validate_integers(sample_value_1))
    print(sanitize_and_validate_integers(sample_value_2))
    print(sanitize_and_validate_integers(sample_value_3))
    print(sanitize_and_validate_integers(sample_value_4))