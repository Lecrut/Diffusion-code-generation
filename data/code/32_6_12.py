class BinaryConverter:
    @staticmethod
    def binary_to_hex(binary_str: str) -> str:
        return hex(int(binary_str, 2))[2:].upper()

if __name__ == '__main__':
    converter = BinaryConverter()
    print(converter.binary_to_hex("10101010"))
    print(converter.binary_to_hex("11110000"))