VALID_BINARY_CHARS = {'0', '1'}

class BinaryValidationError(Exception):
    def __init__(self, message, offending_char=None):
        self.offending_char = offending_char
        super().__init__(message)

def check_validity(binary_string):
    if not isinstance(binary_string, str):
        raise BinaryValidationError("Input must be a string")
    if len(binary_string) == 0:
        raise BinaryValidationError("Input string cannot be empty")
    for char in binary_string:
        if char not in VALID_BINARY_CHARS:
            raise BinaryValidationError(f"Invalid character '{char}'", offending_char=char)

def binary_to_decimal(binary_string):
    result = 0
    multiplier = 1
    for char in reversed(binary_string):
        if char == '1':
            result += multiplier
        multiplier *= 2
    return result

def decimal_to_hex(decimal_value):
    if decimal_value == 0:
        return '0x0'
    hex_digits = '0123456789abcdef'
    hex_string = ''
    current = decimal_value
    while current > 0:
        remainder = current % 16
        hex_string = hex_digits[remainder] + hex_string
        current = current // 16
    return '0x' + hex_string

def convert_binary_to_hex(binary_input):
    check_validity(binary_input)
    decimal_val = binary_to_decimal(binary_input)
    return decimal_to_hex(decimal_val)

if __name__ == '__main__':
    samples = ['0', '1', '1010', '1111', '100000000']
    for s in samples:
        print(convert_binary_to_hex(s))
    errors_to_test = ['12', 'a', '101 ', '']
    for err in errors_to_test:
        try:
            convert_binary_to_hex(err)
        except BinaryValidationError as e:
            print(f"Error: {e}")