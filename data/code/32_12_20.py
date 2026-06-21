class BinaryHexConverter:
    @staticmethod
    def convert(binary_str: str) -> str:
        if not binary_str:
            raise ValueError("Input string cannot be empty")
        try:
            decimal_value = int(binary_str, 2)
        except ValueError:
            raise ValueError("Invalid binary string")
        hex_result = hex(decimal_value)
        return hex_result

if __name__ == '__main__':
    converter = BinaryHexConverter()
    result = converter.convert('101010')
    print(result)