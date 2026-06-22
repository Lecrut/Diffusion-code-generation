class ExtractionError(Exception):
    def __init__(self, message):
        super().__init__(message)

def scan_for_digits(source_string):
    found_digits = []
    for char in source_string:
        if char.isdigit():
            found_digits.append(char)
    return found_digits

def assemble_digit_string(mixed_input):
    extracted = scan_for_digits(mixed_input)
    if not extracted:
        raise ExtractionError("The input string does not contain any digits.")
    return "".join(extracted)

if __name__ == '__main__':
    test_input_alpha_numeric = "Order#A99-X22-Confirm"
    test_input_no_digits = "Status: Pending"
    test_input_all_digits = "1234567890"
    
    print(assemble_digit_string(test_input_alpha_numeric))
    
    try:
        assemble_digit_string(test_input_no_digits)
    except ExtractionError as error:
        print(error)
        
    print(assemble_digit_string(test_input_all_digits))