class BinaryConverter:
    NIBBLE_SIZE = 4
    HEX_CHARS = '0123456789ABCDEF'

    def __init__(self):
        self._nibble_map = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3",
            "0100": "4", "0101": "5", "0110": "6", "0111": "7",
            "1000": "8", "1001": "9", "1010": "A", "1011": "B",
            "1100": "C", "1101": "D", "1110": "E", "1111": "F"
        }

    def convert(self, binary_string: str) -> str:
        if not binary_string:
            return ""
        
        padding_needed = len(binary_string) % self.NIBBLE_SIZE
        if padding_needed:
            binary_string = binary_string.zfill(len(binary_string) + self.NIBBLE_SIZE - padding_needed)
        
        result_parts = []
        for i in range(0, len(binary_string), self.NIBBLE_SIZE):
            chunk = binary_string[i : i + self.NIBBLE_SIZE]
            result_parts.append(self._nibble_map[chunk])
        
        return "".join(result_parts)

if __name__ == "__main__":
    converter = BinaryConverter()
    test_value_1 = "1010111100001111"
    test_value_2 = "1"
    test_value_3 = "0000000000000000"
    test_value_4 = "11111111111111111111"
    
    print(converter.convert(test_value_1))
    print(converter.convert(test_value_2))
    print(converter.convert(test_value_3))
    print(converter.convert(test_value_4))