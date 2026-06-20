class EmptyDigitResult(Exception):
    def __init__(self, message):
        super().__init__(message)

def extract_digits_only(source_text):
    digit_chars = []
    for character in source_text:
        if character.isdigit():
            digit_chars.append(character)
    if not digit_chars:
        raise EmptyDigitResult("The provided string contains no numeric digits.")
    joined_digits = "".join(digit_chars)
    return joined_digits

if __name__ == '__main__':
    sample_input_a = "phone: 555-0192 ext 4"
    sample_input_b = "no numbers here"
    sample_input_c = "1a2b3c"
    try:
        output_a = extract_digits_only(sample_input_a)
        print(output_a)
    except EmptyDigitResult as error:
        print(error)
    try:
        output_b = extract_digits_only(sample_input_b)
        print(output_b)
    except EmptyDigitResult as error:
        print(error)
    try:
        output_c = extract_digits_only(sample_input_c)
        print(output_c)
    except EmptyDigitResult as error:
        print(error)