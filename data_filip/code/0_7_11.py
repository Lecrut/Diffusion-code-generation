class EmptyDigitResultError(Exception):
    def __init__(self, message):
        super().__init__(message)

def filter_numeric_characters(source_text):
    return [char for char in source_text if char.isdigit()]

def extract_and_join_digits(mixed_input):
    numeric_chars = filter_numeric_characters(mixed_input)
    if not numeric_chars:
        raise EmptyDigitResultError("No numeric characters found in input")
    joined_result = "".join(numeric_chars)
    return joined_result

if __name__ == '__main__':
    test_strings = [
        "abc123def456",
        "no digits in this string",
        "007jamesbond",
        "purely alphabetic"
    ]
    for sample_input in test_strings:
        try:
            extracted_value = extract_and_join_digits(sample_input)
            print(extracted_value)
        except EmptyDigitResultError as error:
            print(str(error))