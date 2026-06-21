import binascii

class BinaryToHexConverter:
    def __init__(self):
        self.binary_list = [
            "1010",
            "1111",
            "0000",
            "10010010",
            "11111111",
            "0",
            "10101010",
            "1100110011001100"
        ]

    def validate_binary(self, binary_str):
        if not binary_str:
            raise ValueError("Empty string provided")
        for char in binary_str:
            if char not in ('0', '1'):
                raise ValueError(f"Invalid character '{char}' in binary string")

    def convert_list(self):
        results = []
        for binary_str in self.binary_list:
            try:
                self.validate_binary(binary_str)
                hex_value = format(int(binary_str, 2), 'X')
                results.append(hex_value)
            except ValueError as e:
                raise ValueError(f"Error processing '{binary_str}': {str(e)}")
        return results

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    print(converter.convert_list())