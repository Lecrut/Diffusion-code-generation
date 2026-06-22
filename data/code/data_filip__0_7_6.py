class DigitExtractionFailure(Exception):
    def __init__(self, text):
        super().__init__(f"DigitExtractionFailure: The string '{text}' contains no digits.")

def isolate_numerals(source):
    numeric_part = []
    for index in range(len(source)):
        symbol = source[index]
        if symbol in "0123456789":
            numeric_part.append(symbol)
    return numeric_part

def format_digit_sequence(raw_input):
    collected_chars = isolate_numerals(raw_input)
    total_count = len(collected_chars)
    if total_count == 0:
        raise DigitExtractionFailure(raw_input)
    final_output = "".join(collected_chars)
    return final_output

def run_extraction_workflow():
    input_one = "Data_2023_Version"
    input_two = "Alpha Beta Gamma"
    input_three = "100200300"
    input_four = "NoNumbers!"
    print(format_digit_sequence(input_one))
    print(format_digit_sequence(input_two))
    print(format_digit_sequence(input_three))
    try:
        format_digit_sequence(input_four)
    except DigitExtractionFailure as error:
        print(error)

if __name__ == '__main__':
    run_extraction_workflow()