def clean_and_verify_integers(s):
    translation_table = str.maketrans('', '', ''.join(chr(i) for i in range(256) if not chr(i).isdigit()))
    cleaned = s.translate(translation_table)
    if not cleaned:
        return False
    return cleaned.isdigit()

if __name__ == '__main__':
    sample_values = [
        "12345",
        "123.45",
        "abc123",
        "  456  ",
        "1,234",
        "",
        "100% pure"
    ]
    for value in sample_values:
        result = clean_and_verify_integers(value)
        print(result)