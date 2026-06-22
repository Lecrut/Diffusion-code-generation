class EmptyDigitResultError(Exception):
    def __init__(self, message):
        super().__init__(message)

CHARACTER_ENCODING_OFFSET = ord('0')

def is_digit_character(character):
    code = ord(character)
    return CHARACTER_ENCODING_OFFSET <= code <= CHARACTER_ENCODING_OFFSET + 9

def isolate_numeric_characters(source_text):
    numeric_sequence = []
    for item in source_text:
        if is_digit_character(item):
            numeric_sequence.append(item)
    return numeric_sequence

def extract_and_concatenate_digits(input_value):
    extracted_numbers = isolate_numeric_characters(input_value)
    if not extracted_numbers:
        raise EmptyDigitResultError("No digits were detected in the provided string.")
    return "".join(extracted_numbers)

if __name__ == '__main__':
    first_sample = "test123string456"
    second_sample = "only letters here"
    third_sample = "0000"

    try:
        output_one = extract_and_concatenate_digits(first_sample)
        print(output_one)
    except EmptyDigitResultError as exception_object:
        print(exception_object)

    try:
        output_two = extract_and_concatenate_digits(second_sample)
        print(output_two)
    except EmptyDigitResultError as exception_object:
        print(exception_object)

    try:
        output_three = extract_and_concatenate_digits(third_sample)
        print(output_three)
    except EmptyDigitResultError as exception_object:
        print(exception_object)