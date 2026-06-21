class BinaryHexConverter:
    @staticmethod
    def binary_to_hex(binary_string):
        if not binary_string or not all(c in '01' for c in binary_string):
            raise ValueError("Invalid binary string")
        return hex(int(binary_string, 2))[2:]

if __name__ == '__main__':
    converter = BinaryHexConverter()
    result1 = converter.binary_to_hex('1101')
    print(result1)
    result2 = converter.binary_to_hex('11110000')
    print(result2)
    result3 = converter.binary_to_hex('10101010')
    print(result3)