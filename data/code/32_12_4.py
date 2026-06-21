class BinaryConverter:
    @staticmethod
    def binary_to_hex(binary_string):
        decimal_value = int(binary_string, 2)
        return hex(decimal_value)[2:].upper()

if __name__ == '__main__':
    converter = BinaryConverter()
    sample_binary = "101101"
    result = converter.binary_to_hex(sample_binary)
    print(result)