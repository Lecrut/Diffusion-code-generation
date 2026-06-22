class BinaryToHexConverter:
    @staticmethod
    def convert(binary_sequence: str) -> str:
        if not binary_sequence:
            raise ValueError("Binary sequence cannot be empty")
        
        for char in binary_sequence:
            if char not in '01':
                raise ValueError("Invalid character in binary sequence")
        
        decimal_value = int(binary_sequence, 2)
        hex_string = hex(decimal_value)[2:]
        
        return hex_string.upper()

if __name__ == '__main__':
    converter = BinaryToHexConverter()
    result = converter.convert("101010")
    print(result)