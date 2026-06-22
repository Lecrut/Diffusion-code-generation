class CustomDigitExtractionError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"DigitExtractionError: {value}")

def get_numeric_characters(text):
    result = []
    for char in text:
        if char in '0123456789':
            result.append(char)
    return result

def process_string_for_digits(input_text):
    chars = get_numeric_characters(input_text)
    if not chars:
        raise CustomDigitExtractionError("No digits found")
    return ''.join(chars)

if __name__ == '__main__':
    sample1 = "abc123"
    print(process_string_for_digits(sample1))
    sample2 = "xyz"
    try:
        process_string_for_digits(sample2)
    except CustomDigitExtractionError as e:
        print(e.value)
    sample3 = "98765"
    print(process_string_for_digits(sample3))