class NoDigitsFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)

DIGIT_FILTER_CHARS = "0123456789"

def is_valid_digit(character):
    return character in DIGIT_FILTER_CHARS

def scan_for_digits(input_text):
    extracted_list = []
    for symbol in input_text:
        if is_valid_digit(symbol):
            extracted_list.append(symbol)
    return extracted_list

def assemble_digit_string(input_text):
    gathered_digits = scan_for_digits(input_text)
    if len(gathered_digits) == 0:
        raise NoDigitsFoundError("The provided string contains no numeric digits.")
    return "".join(gathered_digits)

if __name__ == '__main__':
    valid_sample = "Order #442-99: shipped to Zone 7"
    invalid_sample = "No numbers in this line of text"
    
    result_one = assemble_digit_string(valid_sample)
    print(result_one)
    
    try:
        assemble_digit_string(invalid_sample)
    except NoDigitsFoundError as error:
        print(error)
    
    another_test = "v1.0.45"
    print(assemble_digit_string(another_test))