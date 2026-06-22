import string

def clean_and_verify_number(input_string):
    remove_chars = "".join([chr(i) for i in range(256) if chr(i).isdigit() or chr(i) == "-"])
    translation_table = str.maketrans("", "", remove_chars.replace("-", ""))
    cleaned = input_string.translate(translation_table)
    cleaned = cleaned.strip("-")
    if cleaned == "":
        return None
    try:
        return int(cleaned)
    except ValueError:
        return None

if __name__ == '__main__':
    test_input = "  -123abc!@#456  "
    result = clean_and_verify_number(test_input)
    print(result)
    
    test_input_2 = "789.0"
    result_2 = clean_and_verify_number(test_input_2)
    print(result_2)
    
    test_input_3 = "12a34"
    result_3 = clean_and_verify_number(test_input_3)
    print(result_3)