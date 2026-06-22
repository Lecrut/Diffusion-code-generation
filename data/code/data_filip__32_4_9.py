BINARY_VALID_CHARS = frozenset({'0', '1'})

class InvalidBinaryInputError(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_binary_format(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Expected string input")
    for index, character in enumerate(input_string):
        if character not in BINARY_VALID_CHARS:
            raise InvalidBinaryInputError(f"Invalid character '{character}' at index {index}")

def convert_binary_string_to_hex(binary_input):
    check_binary_format(binary_input)
    if len(binary_input) == 0:
        return '0x0'
    integer_value = int(binary_input, 2)
    return hex(integer_value)

if __name__ == '__main__':
    test_values = ["1010", "11110000", "0", "1", "1101110110110111"]
    for val in test_values:
        result = convert_binary_string_to_hex(val)
        print(result)

    error_values = ["102", "hello", "10.1", "", "111 000"]
    for err_val in error_values:
        try:
            convert_binary_string_to_hex(err_val)
        except (InvalidBinaryInputError, TypeError) as ex:
            print(str(ex))