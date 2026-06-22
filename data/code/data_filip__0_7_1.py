class MissingDigitsError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def get_digit_chars(text):
    result = []
    for character in text:
        if character.isdigit():
            result.append(character)
    return result

def extract_and_concatenate_digits(input_string):
    found_digits = get_digit_chars(input_string)
    if len(found_digits) == 0:
        raise MissingDigitsError("Input does not contain any numeric characters")
    final_string = "".join(found_digits)
    return final_string

if __name__ == '__main__':
    test_data_1 = "a1b2c3"
    test_data_2 = "hello world"
    test_data_3 = "09876"
    
    output_1 = extract_and_concatenate_digits(test_data_1)
    print(output_1)
    
    try:
        extract_and_concatenate_digits(test_data_2)
    except MissingDigitsError as error_instance:
        print(str(error_instance))
        
    output_3 = extract_and_concatenate_digits(test_data_3)
    print(output_3)