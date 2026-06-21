class BinaryToHexConverter:
    @staticmethod
    def convert(binary_string):
        return hex(int(binary_string, 2))[2:]

    @staticmethod
    def convert_list(binary_list):
        return [hex(int(b, 2))[2:] for b in binary_list]

    @staticmethod
    def validate_binary(binary_string):
        try:
            int(binary_string, 2)
            return True
        except ValueError:
            return False

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    print(converter.convert('1010'))
    print(converter.convert('11110000'))
    print(converter.convert_list(['1010', '1100', '1111']))
    print(converter.validate_binary('1010'))
    print(converter.validate_binary('1210'))