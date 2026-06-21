class InvalidBinaryError(Exception):
    def __init__(self, message, character=None):
        self.character = character
        super().__init__(message)

def validate_binary_string(input_str):
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    if len(input_str) == 0:
        raise InvalidBinaryError("Input string cannot be empty")
    for index, char in enumerate(input_str):
        if char != '0' and char != '1':
            raise InvalidBinaryError(f"Invalid character '{char}' at position {index}", character=char)
    return True

def binary_to_hexadecimal(binary_str):
    validate_binary_string(binary_str)
    decimal_value = int(binary_str, 2)
    return hex(decimal_value)

if __name__ == '__main__':
    valid_cases = ["0", "1", "1010", "11111111", "1000000000000"]
    for case in valid_cases:
        try:
            result = binary_to_hexadecimal(case)
            print(f"{case} -> {result}")
        except Exception as e:
            print(f"Error processing {case}: {e}")
    
    invalid_cases = ["2", "10a1", "", "10 01", "010x"]
    for case in invalid_cases:
        try:
            result = binary_to_hexadecimal(case)
            print(f"{case} -> {result}")
        except (TypeError, InvalidBinaryError) as e:
            if hasattr(e, 'character') and e.character:
                print(f"Caught InvalidBinaryError for '{case}': character '{e.character}' is invalid")
            else:
                print(f"Caught Exception for '{case}': {e}")