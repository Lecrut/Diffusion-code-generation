class EmptyDigitSetError(Exception):
    def __init__(self, message="No digits were found in the provided string"):
        super().__init__(message)

def extract_and_concatenate_numeric_characters(source_text):
    numeric_chars = []
    for character in source_text:
        if character in "0123456789":
            numeric_chars.append(character)
    if not numeric_chars:
        raise EmptyDigitSetError()
    concatenated_result = "".join(numeric_chars)
    return concatenated_result

if __name__ == "__main__":
    test_input_with_numbers = "abc123def45gh6"
    test_input_without_numbers = "xyzqrs"
    test_input_only_numbers = "102030"

    output_a = extract_and_concatenate_numeric_characters(test_input_with_numbers)
    print(output_a)

    try:
        output_b = extract_and_concatenate_numeric_characters(test_input_without_numbers)
        print(output_b)
    except EmptyDigitSetError as err:
        print(err)

    output_c = extract_and_concatenate_numeric_characters(test_input_only_numbers)
    print(output_c)