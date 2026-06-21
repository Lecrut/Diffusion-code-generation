class InvalidBinaryCharacterError(Exception):
    def __init__(self, message, invalid_char, position):
        self.invalid_char = invalid_char
        self.position = position
        super().__init__(message)

def is_valid_binary_char(char):
    return char == '0' or char == '1'

def validate_binary_input(binary_string):
    if not isinstance(binary_string, str):
        raise TypeError("Input must be a string")
    if len(binary_string) == 0:
        raise ValueError("Input string cannot be empty")
    for index, char in enumerate(binary_string):
        if not is_valid_binary_char(char):
            raise InvalidBinaryCharacterError(
                f"Found invalid character '{char}' at index {index}",
                invalid_char=char,
                position=index
            )
    return True

def convert_binary_to_hex(binary_string):
    validate_binary_input(binary_string)
    decimal_value = int(binary_string, 2)
    return hex(decimal_value)

def process_sample_list(samples):
    results = []
    for sample in samples:
        try:
            converted = convert_binary_to_hex(sample)
            results.append(f"Success: '{sample}' -> {converted}")
        except Exception as e:
            results.append(f"Error: '{sample}' -> {type(e).__name__}: {e}")
    return results

if __name__ == '__main__':
    valid_samples = ["0", "1", "1010", "11110000", "000100101101"]
    invalid_samples = ["102", "0x1", "101a", "11.01", ""]
    all_test_cases = valid_samples + invalid_samples
    output = process_sample_list(all_test_cases)
    for line in output:
        print(line)