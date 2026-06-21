class BinaryToHexConverter:
    @staticmethod
    def convert(binary_sequence: str) -> str:
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Invalid binary sequence")
        decimal_value = int(binary_sequence, 2)
        return hex(decimal_value)[2:].upper()

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    print(converter.convert("1010"))
    print(converter.convert("11110000"))
    print(converter.convert("11011011"))