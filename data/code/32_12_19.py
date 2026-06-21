class BinaryHexConverter:
    @staticmethod
    def bin_to_hex(binary_string):
        if not binary_string:
            return '0x0'
        number = int(binary_string, 2)
        return hex(number)

if __name__ == '__main__':
    converter = BinaryHexConverter()
    sample_bin = '1101'
    result = converter.bin_to_hex(sample_bin)
    print(result)
    another_bin = '11110000'
    result2 = converter.bin_to_hex(another_bin)
    print(result2)