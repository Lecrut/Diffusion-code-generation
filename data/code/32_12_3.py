class BinaryToHexConverter:
    @staticmethod
    def convert(binary_string: str) -> str:
        decimal_value = int(binary_string, 2)
        hex_value = hex(decimal_value)
        return hex_value

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    binary_input = "101010"
    result = converter.convert(binary_input)
    print(result)