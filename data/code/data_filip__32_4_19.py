BINARY_ALLOWED = frozenset({'0', '1'})

class BinaryValidationError(ValueError):
    def __init__(self, message, invalid_char=None):
        self.invalid_char = invalid_char
        super().__init__(message)

def _check_character_validity(char):
    if char not in BINARY_ALLOWED:
        raise BinaryValidationError(f"Found non-binary character: {char}", invalid_char=char)

def _validate_binary_string(data):
    if not isinstance(data, str):
        raise TypeError("Expecting string input for binary data")
    if len(data) == 0:
        raise BinaryValidationError("Binary string must not be empty")
    for item in data:
        _check_character_validity(item)

def convert_binary_to_hex(binary_data):
    _validate_binary_string(binary_data)
    integer_value = int(binary_data, 2)
    return hex(integer_value)

if __name__ == '__main__':
    valid_samples = ["1010", "11110000", "0", "11111111", "10101010"]
    for sample in valid_samples:
        result = convert_binary_to_hex(sample)
        print(result)
    invalid_samples = ["1020", "111a", "", "1 0"]
    for sample in invalid_samples:
        try:
            convert_binary_to_hex(sample)
        except Exception as e:
            print(f"Error handling '{sample}': {type(e).__name__}: {e}")