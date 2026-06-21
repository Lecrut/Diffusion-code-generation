VALID_CHARS = {'0', '1'}
HEX_MAP = {
    '0000': '0',
    '0001': '1',
    '0010': '2',
    '0011': '3',
    '0100': '4',
    '0101': '5',
    '0110': '6',
    '0111': '7',
    '1000': '8',
    '1001': '9',
    '1010': 'A',
    '1011': 'B',
    '1100': 'C',
    '1101': 'D',
    '1110': 'E',
    '1111': 'F'
}

class BinaryConversionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_binary_string(data):
    if not isinstance(data, str):
        raise BinaryConversionError("Input must be a string type")
    for character in data:
        if character not in VALID_CHARS:
            raise BinaryConversionError("Invalid character found: " + character)
    return True

def pad_binary_string(data):
    remainder = len(data) % 4
    if remainder != 0:
        padding_needed = 4 - remainder
        padded = '0' * padding_needed + data
        return padded
    return data

def convert_chunk(chunk):
    return HEX_MAP[chunk]

def binary_to_hex_converter(binary_input):
    validate_binary_string(binary_input)
    if binary_input == '':
        return '0x0'
    padded = pad_binary_string(binary_input)
    chunks = []
    for i in range(0, len(padded), 4):
        chunk = padded[i:i+4]
        chunks.append(convert_chunk(chunk))
    hex_digits = ''.join(chunks)
    return '0x' + hex_digits

if __name__ == '__main__':
    test_cases_valid = [
        '1010',
        '1111',
        '1',
        '10000000',
        '11001100'
    ]
    for case in test_cases_valid:
        result = binary_to_hex_converter(case)
        print(case, result)
    
    test_cases_invalid = [
        '102',
        'abc',
        '101 01',
        '10.01',
        1010
    ]
    for case in test_cases_invalid:
        try:
            binary_to_hex_converter(case)
        except BinaryConversionError as error:
            print("Error for", repr(case), ":", error.message)