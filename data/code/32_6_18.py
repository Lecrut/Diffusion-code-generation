class BinaryHexConverter:
    @staticmethod
    def binary_to_hex(binary_str: str) -> str:
        try:
            if not isinstance(binary_str, str):
                raise TypeError("Input must be a string")
            
            if not all(c in '01' for c in binary_str):
                raise ValueError("Input string must contain only '0' and '1'")
            
            if not binary_str:
                return "0"
            
            decimal_value = int(binary_str, 2)
            hex_string = hex(decimal_value)[2:].upper()
            
            return hex_string
        except Exception as e:
            raise type(e)(str(e))

if __name__ == '__main__':
    converter = BinaryHexConverter()
    result = converter.binary_to_hex("1101")
    print(result)
    
    result2 = converter.binary_to_hex("11111111")
    print(result2)
    
    result3 = converter.binary_to_hex("10101010")
    print(result3)