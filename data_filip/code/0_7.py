class NoDigitsError(Exception):
    def __init__(self, message):
        super().__init__(message)

def extract_digits_and_join(mixed_string):
    digits = [char for char in mixed_string if char.isdigit()]
    if not digits:
        raise NoDigitsError("No digits found in the input string.")
    return "".join(digits)

if __name__ == '__main__':
    sample_text_1 = "abc123xyz45"
    sample_text_2 = "no_digits_here"
    sample_text_3 = "9876543210"
    try:
        result1 = extract_digits_and_join(sample_text_1)
        print(result1)
    except NoDigitsError as e:
        print(e)
    try:
        result2 = extract_digits_and_join(sample_text_2)
        print(result2)
    except NoDigitsError as e:
        print(e)
    try:
        result3 = extract_digits_and_join(sample_text_3)
        print(result3)
    except NoDigitsError as e:
        print(e)