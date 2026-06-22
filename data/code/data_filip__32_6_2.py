class BinaryConverter:
    @staticmethod
    def binary_to_hex(binary_string: str) -> str:
        cleaned = binary_string.replace(" ", "").replace("\t", "").replace("\n", "")
        if not cleaned:
            return "0x0"
        for char in cleaned:
            if char not in ("0", "1"):
                raise ValueError(f"Invalid binary character: {char}")
        decimal_value = int(cleaned, 2)
        hex_string = hex(decimal_value)
        return hex_string

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_binary = "11010110"
    result = converter.binary_to_hex(sample_binary)
    print(result)
    sample_binary_zero = "0"
    result_zero = converter.binary_to_hex(sample_binary_zero)
    print(result_zero)
    sample_binary_large = "111111111111"
    result_large = converter.binary_to_hex(sample_binary_large)
    print(result_large)