class BinaryHexManager:
    @staticmethod
    def convert_binary_to_hex(binary_string: str) -> str:
        if not binary_string:
            return "0x0"
        integer_value = int(binary_string, 2)
        return hex(integer_value)

if __name__ == '__main__':
    sample_binary = "1010110011001111"
    manager = BinaryHexManager()
    result = manager.convert_binary_to_hex(sample_binary)
    print(result)
    another_result = BinaryHexManager.convert_binary_to_hex("11111111")
    print(another_result)
    zero_result = BinaryHexManager.convert_binary_to_hex("0")
    print(zero_result)