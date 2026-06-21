def clean_and_verify_integer_string(s):
    chars_to_remove = "".join(chr(c) for c in range(128) if not chr(c).isdigit() and chr(c) not in "-+")
    translation_table = str.maketrans("", "", chars_to_remove)
    cleaned = s.translate(translation_table)
    cleaned = cleaned.strip("-+")
    if not cleaned:
        return False
    try:
        int(cleaned)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    test_strings = ["123abc456", "-789", "+101", "12.34", "42"]
    for s in test_strings:
        result = clean_and_verify_integer_string(s)
        print(result)