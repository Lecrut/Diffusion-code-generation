class DigitNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

DIGIT_MIN = 0
DIGIT_MAX = 9

def validate_has_digits(char_list):
    if len(char_list) == 0:
        raise DigitNotFoundException("The provided string contains no numeric digits.")

def build_digit_string(char_list):
    return "".join(char_list)

def extract_and_return_digits(raw_text):
    extracted_chars = []
    for char in raw_text:
        if char.isdigit():
            extracted_chars.append(char)
    validate_has_digits(extracted_chars)
    return build_digit_string(extracted_chars)

if __name__ == '__main__':
    test_string_1 = "Order_99x2024"
    test_string_2 = "alpha_beta_gamma"
    test_string_3 = "v2.0.1_patch"

    print(extract_and_return_digits(test_string_1))

    try:
        extract_and_return_digits(test_string_2)
    except DigitNotFoundException as error:
        print(str(error))

    print(extract_and_return_digits(test_string_3))