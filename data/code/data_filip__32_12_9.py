class BinaryToHexConverter:
    @staticmethod
    def convert(binary_str: str) -> str:
        if not binary_str:
            return ''
        decimal_value = int(binary_str, 2)
        hex_result = hex(decimal_value)[2:]
        return hex_result

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    sample_binary = "10101010"
    result = converter.convert(sample_binary)
    print(result)