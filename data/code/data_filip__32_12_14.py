class BinaryHexManager:
    @staticmethod
    def convert_binary_to_hex(binary_string):
        if not binary_string:
            return "0x0"
        decimal_value = int(binary_string, 2)
        hex_value = hex(decimal_value)
        return hex_value

if __name__ == '__main__':
    manager = BinaryHexManager()
    sample_binary = "11011011"
    result = manager.convert_binary_to_hex(sample_binary)
    print(result)
    print(manager.convert_binary_to_hex("1010"))
    print(manager.convert_binary_to_hex("11111111"))