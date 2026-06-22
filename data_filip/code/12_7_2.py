import string

def clean_and_verify_integer(raw_data):
    formatter_chars = string.whitespace + string.punctuation
    translator = str.maketrans('', '', formatter_chars)
    cleaned_data = raw_data.translate(translator)
    if cleaned_data == '':
        return False
    try:
        int(cleaned_data)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    test_input_1 = "  12345  "
    test_input_2 = "12a34"
    test_input_3 = "1,000,000"
    result_1 = clean_and_verify_integer(test_input_1)
    result_2 = clean_and_verify_integer(test_input_2)
    result_3 = clean_and_verify_integer(test_input_3)
    print(result_1)
    print(result_2)
    print(result_3)