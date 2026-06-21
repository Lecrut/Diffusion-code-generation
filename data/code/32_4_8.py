class BinaryValidationException(Exception):
    def __init__(self, message, bad_char=None):
        self.bad_char = bad_char
        super().__init__(message)

class BinaryToHexConverter:
    ALLOWED_CHARS = frozenset({'0', '1'})

    def __init__(self):
        self._lookup = {
            '0000': '0', '0001': '1', '0010': '2', '0011': '3',
            '0100': '4', '0101': '5', '0110': '6', '0111': '7',
            '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
            '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
        }

    def validate(self, data):
        if not isinstance(data, str):
            raise TypeError("Expected string input")
        for char in data:
            if char not in self.ALLOWED_CHARS:
                raise BinaryValidationException(f"Invalid binary character: {char}", bad_char=char)
        return True

    def convert(self, binary_str):
        self.validate(binary_str)
        if not binary_str:
            return "0"
        remainder = len(binary_str) % 4
        if remainder:
            padded = binary_str.zfill(len(binary_str) + (4 - remainder))
        else:
            padded = binary_str
        hex_chars = []
        for i in range(0, len(padded), 4):
            nibble = padded[i:i+4]
            hex_chars.append(self._lookup[nibble])
        result = "".join(hex_chars)
        stripped = result.lstrip('0')
        return stripped if stripped else "0"

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    valid_inputs = ["1010", "1111", "0", "10101010", "1"]
    for val in valid_inputs:
        print(converter.convert(val))
    invalid_inputs = ["102", "abc", "1 0", "0x1"]
    for bad_val in invalid_inputs:
        try:
            converter.convert(bad_val)
        except BinaryValidationException as e:
            print(e)