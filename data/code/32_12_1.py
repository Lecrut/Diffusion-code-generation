class BinaryConverter:
    @staticmethod
    def convert(binary_string):
        decimal_value = int(binary_string, 2)
        return hex(decimal_value)

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_binary = '1101'
    result = converter.convert(sample_binary)
    print(result)
    sample_binary_2 = '101010'
    result_2 = converter.convert(sample_binary_2)
    print(result_2)