class BinaryToHexConverter:
    @staticmethod
    def convert(binary_sequence: str) -> str:
        if not isinstance(binary_sequence, str):
            raise TypeError("Input must be a string")
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input must contain only '0' and '1'")
        if not binary_sequence:
            return "0"
        decimal_value = int(binary_sequence, 2)
        return format(decimal_value, 'X')

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    print(converter.convert("1010"))
    print(converter.convert("11110000"))
    print(converter.convert("0"))
    print(converter.convert("11111111"))