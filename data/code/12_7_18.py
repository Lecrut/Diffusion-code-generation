import string

def sanitize_and_validate_integers(input_string):
    translation_table = str.maketrans('', '', string.punctuation + string.whitespace)
    cleaned_string = input_string.translate(translation_table)
    if not cleaned_string:
        return False
    try:
        int(cleaned_string)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    sample1 = "123"
    sample2 = "12,345"
    sample3 = "abc123"
    sample4 = "123 456"
    sample5 = "999"
    result1 = sanitize_and_validate_integers(sample1)
    result2 = sanitize_and_validate_integers(sample2)
    result3 = sanitize_and_validate_integers(sample3)
    result4 = sanitize_and_validate_integers(sample4)
    result5 = sanitize_and_validate_integers(sample5)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)