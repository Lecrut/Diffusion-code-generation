def clean_and_verify_integers(raw_string):
    translation_table = str.maketrans('', '', ' \t\n\r,;:.()[]{}+-_!?@#$%^&*|"\'`~')
    cleaned = raw_string.translate(translation_table)
    if not cleaned:
        return False
    for char in cleaned:
        if char not in '0123456789':
            return False
    return True

if __name__ == '__main__':
    test_strings = [
        " 123,456 ",
        "12.34",
        "123abc",
        "-567",
        "007",
        ""
    ]
    for s in test_strings:
        result = clean_and_verify_integers(s)
        print(result)