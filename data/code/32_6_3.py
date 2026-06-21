class BinaryConverter:
    @staticmethod
    def to_hex(binary_sequence: str) -> str:
        if not isinstance(binary_sequence, str):
            raise TypeError("Input must be a string")
        if not binary_sequence:
            return "0"
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input string must contain only 0s and 1s")
        decimal_value = int(binary_sequence, 2)
        hex_string = hex(decimal_value)[2:]
        return hex_string

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_binary = "1101101"
    result = converter.to_hex(sample_binary)
    print(result)