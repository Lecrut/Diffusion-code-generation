class ExtractedDigitsNotFound(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"ExtractedDigitsNotFound: {value}")

def retrieve_numeric_characters(input_data):
    digits = []
    for current_char in input_data:
        if current_char.isdigit():
            digits.append(current_char)
    if not digits:
        raise ExtractedDigitsNotFound("No digits found in the input string.")
    return "".join(digits)

if __name__ == '__main__':
    sample_one = "abc123xyz45"
    sample_two = "no_digits_here"
    sample_three = "9876543210"
    sample_four = "a1b2c3"
    sample_five = "hello world"

    result1 = retrieve_numeric_characters(sample_one)
    print(result1)

    try:
        retrieve_numeric_characters(sample_two)
    except ExtractedDigitsNotFound as e:
        print(e)

    result2 = retrieve_numeric_characters(sample_three)
    print(result2)

    result3 = retrieve_numeric_characters(sample_four)
    print(result3)

    try:
        retrieve_numeric_characters(sample_five)
    except ExtractedDigitsNotFound as e:
        print(e)