class InvalidBinaryCharacterError(Exception):
    def __init__(self, message, bad_char, position):
        self.bad_char = bad_char
        self.position = position
        super().__init__(message)

VALID_BINARY_SET = frozenset(('0', '1'))

def validate_binary_input(binary_string):
    if not isinstance(binary_string, str):
        raise TypeError("Input must be a string")
    if len(binary_string) == 0:
        raise ValueError("Input string cannot be empty")
    for index, char in enumerate(binary_string):
        if char not in VALID_BINARY_SET:
            raise InvalidBinaryCharacterError(
                f"Invalid character '{char}' found at index {index}",
                char,
                index
            )
    return True

def convert_binary_to_hex(binary_string):
    if validate_binary_input(binary_string):
        decimal_value = int(binary_string, 2)
        return hex(decimal_value)[2:].upper()

def main():
    valid_cases = ["1010", "1111", "0000", "10101010", "1111000011110000"]
    invalid_cases = ["102", "abc", "10101 0011", "10.01", ""]
    
    for case in valid_cases:
        result = convert_binary_to_hex(case)
        print(f"Valid: {case} -> {result}")
    
    for case in invalid_cases:
        try:
            result = convert_binary_to_hex(case)
            print(f"Unexpected success for '{case}': {result}")
        except InvalidBinaryCharacterError as e:
            print(f"Caught specific error for '{case}': {e}")
        except (ValueError, TypeError) as e:
            print(f"Caught general error for '{case}': {e}")

if __name__ == '__main__':
    main()