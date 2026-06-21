import string

def sanitize_and_verify_integers(input_str):
    translation_table = str.maketrans('', '', string.punctuation + string.whitespace)
    cleaned_str = input_str.translate(translation_table)
    if not cleaned_str:
        return False
    try:
        int(cleaned_str)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    test_cases = ["123", "45-67", " 890 ", "abc", "12#34"]
    for case in test_cases:
        result = sanitize_and_verify_integers(case)
        print(f"{case} -> {result}")