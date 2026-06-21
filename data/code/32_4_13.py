class BinaryConversionError(Exception):
    def __init__(self, message, invalid_char=None):
        self.invalid_char = invalid_char
        super().__init__(message)

def validate_binary_characters(binary_input):
    if not isinstance(binary_input, str):
        raise TypeError("Input must be a string")
    if len(binary_input) == 0:
        raise BinaryConversionError("Input string cannot be empty")
    for index, char in enumerate(binary_input):
        if char not in ('0', '1'):
            raise BinaryConversionError(f"Invalid character '{char}' at index {index}", invalid_char=char)

def binary_to_hexadecimal(binary_input):
    validate_binary_characters(binary_input)
    decimal_value = int(binary_input, 2)
    return format(decimal_value, 'X')

if __name__ == '__main__':
    valid_inputs = ["1010", "1111", "0000", "10010101", "11001100", "1"]
    invalid_inputs = ["102", "abc", "10101 0011", "10.01", ""]
    
    for valid_input in valid_inputs:
        result = binary_to_hexadecimal(valid_input)
        print(f"{valid_input} -> {result}")
    
    for invalid_input in invalid_inputs:
        try:
            binary_to_hexadecimal(invalid_input)
        except BinaryConversionError as e:
            print(f"Error for '{invalid_input}': {e}")
        except TypeError as e:
            print(f"Type Error for '{invalid_input}': {e}")