class NoDigitsError(Exception):
    def __init__(self, message="No digits found in the input string"):
        self.message = message
        super().__init__(self.message)

def extract_digits(s):
    digits = [char for char in s if char.isdigit()]
    if not digits:
        raise NoDigitsError()
    return ''.join(digits)

if __name__ == '__main__':
    sample_string = "a1b2c3"
    result = extract_digits(sample_string)
    print(result)

    try:
        no_digit_string = "abc"
        extract_digits(no_digit_string)
    except NoDigitsError as e:
        print(e.message)