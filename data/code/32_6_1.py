class BinaryHexConverter:
    @staticmethod
    def binary_to_hex(binary_sequence: str) -> str:
        int_value = int(binary_sequence, 2)
        hex_str = hex(int_value)[2:]
        if len(hex_str) % 2 != 0:
            hex_str = '0' + hex_str
        return hex_str.upper()

if __name__ == '__main__':
    converter = BinaryHexConverter()
    binary_input = '11110000'
    result = converter.binary_to_hex(binary_input)
    print(result)