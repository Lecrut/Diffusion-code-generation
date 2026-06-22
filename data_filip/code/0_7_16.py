class MissingNumericCharacters(Exception):
    def __init__(self, message):
        super().__init__(message)

DIGIT_SET = "0123456789"

def build_digit_buffer(source):
    buffer = []
    for symbol in source:
        if symbol in DIGIT_SET:
            buffer.append(symbol)
    return buffer

def extract_and_concatenate_numeric(source):
    numeric_buffer = build_digit_buffer(source)
    if len(numeric_buffer) == 0:
        raise MissingNumericCharacters("Input lacks any numeric characters")
    return "".join(numeric_buffer)

if __name__ == '__main__':
    case_a = "alpha-9-beta-88"
    case_b = "pure-letters-only"
    case_c = "42"
    
    test_cases = [case_a, case_b, case_c]
    
    for item in test_cases:
        try:
            output = extract_and_concatenate_numeric(item)
            print(output)
        except MissingNumericCharacters as err:
            print(err)