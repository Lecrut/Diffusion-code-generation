class BinaryHexConverter:
    @staticmethod
    def binary_to_hex(binary_str):
        if not binary_str:
            return ""
        decimal_value = int(binary_str, 2)
        hex_value = hex(decimal_value)
        return hex_value[2:].upper().zfill(max(1, len(hex_value) - 2))

    def convert(self, binary_str):
        return self.binary_to_hex(binary_str)

if __name__ == '__main__':
    converter = BinaryHexConverter()
    result = converter.convert("1010")
    print(result)
    result2 = converter.convert("11110000")
    print(result2)