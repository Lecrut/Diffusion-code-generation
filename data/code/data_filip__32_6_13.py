class BinaryConverter:
    @staticmethod
    def binary_to_hex(binary_sequence: str) -> str:
        if not binary_sequence:
            return "0"
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input must be a binary string")
        decimal_value = int(binary_sequence, 2)
        hex_string = hex(decimal_value)
        return hex_string.lstrip("0x").upper()

if __name__ == '__main__':
    converter = BinaryConverter()
    result = converter.binary_to_hex("11111111")
    print(result)