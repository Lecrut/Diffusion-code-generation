class BinaryConverter:
    @staticmethod
    def binary_to_hex(binary_str: str) -> str:
        hex_val = int(binary_str, 2)
        return hex(hex_val)[2:].upper()

if __name__ == '__main__':
    converter = BinaryConverter()
    binary_input = "10101100110011011010101011001100"
    result = converter.binary_to_hex(binary_input)
    print(result)