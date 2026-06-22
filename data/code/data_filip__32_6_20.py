class BinaryHexConverter:
    @staticmethod
    def convert_binary_to_hex(binary_sequence: str) -> str:
        if not isinstance(binary_sequence, str):
            raise TypeError("Input must be a string")
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input must contain only binary digits (0 and 1)")
        if not binary_sequence:
            return "0"
        decimal_value = int(binary_sequence, 2)
        hex_string = hex(decimal_value)[2:]
        return hex_string.upper()

if __name__ == '__main__':
    converter = BinaryHexConverter()
    result = converter.convert_binary_to_hex("10101010")
    print(result)
    result2 = converter.convert_binary_to_hex("00001111")
    print(result2)