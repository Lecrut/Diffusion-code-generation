class BinaryToHexConverter:
    @staticmethod
    def binary_to_hex(binary_sequence: str) -> str:
        if not isinstance(binary_sequence, str):
            raise TypeError("Input must be a string")
        if not all(c in '01' for c in binary_sequence):
            raise ValueError("Input must contain only 0s and 1s")
        if len(binary_sequence) == 0:
            return ""
        decimal_value = int(binary_sequence, 2)
        hex_string = format(decimal_value, 'x').upper()
        return hex_string

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    result1 = converter.binary_to_hex('1010')
    print(result1)
    result2 = converter.binary_to_hex('11110000')
    print(result2)
    result3 = converter.binary_to_hex('0')
    print(result3)
    result4 = converter.binary_to_hex('11010110')
    print(result4)