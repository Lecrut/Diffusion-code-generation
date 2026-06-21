class BinaryConverter:
    @staticmethod
    def to_hex(binary_string):
        decimal_value = int(binary_string, 2)
        return hex(decimal_value)

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_binary = '1101011'
    result = converter.to_hex(sample_binary)
    print(result)
    sample_binary_2 = '10101010'
    result_2 = converter.to_hex(sample_binary_2)
    print(result_2)