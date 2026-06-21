class BinaryToHexConverter:
    @staticmethod
    def binary_to_hex(binary_sequence: str) -> str:
        if not isinstance(binary_sequence, str):
            raise TypeError("Input must be a string")
        for char in binary_sequence:
            if char not in ('0', '1'):
                raise ValueError("Input must contain only '0' and '1'")
        if len(binary_sequence) % 4 != 0:
            binary_sequence = binary_sequence.zfill((len(binary_sequence) // 4 + 1) * 4)
        hex_string = hex(int(binary_sequence, 2))[2:].upper()
        return hex_string

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    print(converter.binary_to_hex("10101011"))
    print(converter.binary_to_hex("110011001100"))
    print(converter.binary_to_hex("0"))
    print(converter.binary_to_hex("1111"))