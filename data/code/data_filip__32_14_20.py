class BinaryHexConverter:
    NIBBLE_TABLE = '0123456789ABCDEF'

    @staticmethod
    def convert(binary_string):
        if not binary_string:
            return ""
        remainder = len(binary_string) % 4
        if remainder:
            binary_string = '0' * (4 - remainder) + binary_string
        result_chars = []
        for i in range(0, len(binary_string), 4):
            nibble = binary_string[i : i + 4]
            value = int(nibble, 2)
            result_chars.append(BinaryHexConverter.NIBBLE_TABLE[value])
        return "".join(result_chars)

if __name__ == '__main__':
    converter = BinaryHexConverter()
    test_input = '1111111100000000101010101100110011110000'
    output = converter.convert(test_input)
    print(output)