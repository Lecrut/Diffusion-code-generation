class BinaryConverter:
    @staticmethod
    def to_hex(binary_string):
        decimal_value = int(binary_string, 2)
        return hex(decimal_value)[2:].upper()

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_binary_1 = "1010"
    sample_binary_2 = "11110000"
    result_1 = converter.to_hex(sample_binary_1)
    result_2 = converter.to_hex(sample_binary_2)
    print(result_1)
    print(result_2)