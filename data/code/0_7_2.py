class DigitExtractionError(Exception):
    def __init__(self, message):
        super().__init__(message)

def filter_digits(input_text):
    collected = []
    for char in input_text:
        if char.isdigit():
            collected.append(char)
    return collected

def combine_digits(input_text):
    found = filter_digits(input_text)
    if len(found) == 0:
        raise DigitExtractionError("Failed to extract digits from string")
    return "".join(found)

if __name__ == "__main__":
    test_case_a = "version2.0.1"
    test_case_b = "no_numbers"
    test_case_c = "987"

    print(combine_digits(test_case_a))

    try:
        combine_digits(test_case_b)
    except DigitExtractionError as e:
        print(e)

    print(combine_digits(test_case_c))