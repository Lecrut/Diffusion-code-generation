class BinaryHexConverter:
    @staticmethod
    def binary_to_hex(binary_str):
        if not binary_str:
            return "0x0"
        
        number = int(binary_str, 2)
        hex_str = hex(number)
        
        return hex_str

if __name__ == '__main__':
    samples = [
        "1010",
        "11110000",
        "10000000000",
        "11111111",
        "0",
        "1"
    ]
    
    converter = BinaryHexConverter()
    
    for binary in samples:
        result = converter.binary_to_hex(binary)
        print(f"{binary} -> {result}")