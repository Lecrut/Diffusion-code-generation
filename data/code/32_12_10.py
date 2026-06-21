class BinaryHexConverter:
    @staticmethod
    def binary_to_hex(binary_str):
        return hex(int(binary_str, 2))[2:]

if __name__ == '__main__':
    converter = BinaryHexConverter()
    print(converter.binary_to_hex('1010'))
    print(converter.binary_to_hex('11111111'))
    print(converter.binary_to_hex('100000000'))