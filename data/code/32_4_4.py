class BinaryConversionError(Exception):
    def __init__(self, message, invalid_char=None):
        self.invalid_char = invalid_char
        super().__init__(message)

def validate_and_convert(binary_string):
    if not isinstance(binary_string, str):
        raise BinaryConversionError("Input must be a string")
    if len(binary_string) == 0:
        raise BinaryConversionError("Input string cannot be empty")
    for char in binary_string:
        if char not in ('0', '1'):
            raise BinaryConversionError(f"Invalid character '{char}' found in binary input", invalid_char=char)
    return hex(int(binary_string, 2))

if __name__ == '__main__':
    test_cases = ["1010", "1111", "00000000", "10101010", "1111000011110000"]
    invalid_cases = ["102", "0x1", "101a01", "", "10.1"]
    
    for case in test_cases:
        result = validate_and_convert(case)
        print(f"{case} -> {result}")
    
    for case in invalid_cases:
        try:
            result = validate_and_convert(case)
            print(f"{case} -> {result}")
        except BinaryConversionError as e:
            print(f"Error for '{case}': {e}")