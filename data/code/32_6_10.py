class BinaryHexConverter:
    @staticmethod
    def binary_to_hex(binary_str: str) -> str:
        return hex(int(binary_str, 2))[2:].upper()

if __name__ == '__main__':
    result = BinaryHexConverter.binary_to_hex('101010')
    print(result)