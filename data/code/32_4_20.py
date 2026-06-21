class BinaryToHexConverter:
    def __init__(self, binary_string):
        if not isinstance(binary_string, str):
            raise TypeError("Input must be a string.")
        if not binary_string:
            raise ValueError("Input string cannot be empty.")
        self.binary_string = binary_string

    def validate_and_convert(self):
        if not self.binary_string:
            raise ValueError("Input string cannot be empty.")
        
        valid_chars = set('01')
        for char in self.binary_string:
            if char not in valid_chars:
                raise ValueError(f"Invalid character '{char}' in binary input.")
        
        decimal_value = int(self.binary_string, 2)
        hex_string = hex(decimal_value)[2:]
        
        if len(hex_string) % 2 != 0:
            hex_string = '0' + hex_string
            
        return hex_string.upper()

if __name__ == '__main__':
    try:
        converter = BinaryToHexConverter("11110010")
        result = converter.validate_and_convert()
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")

    try:
        bad_converter = BinaryToHexConverter("111100Z2")
        result = bad_converter.validate_and_convert()
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")

    try:
        int_converter = BinaryToHexConverter(12345)
        result = int_converter.validate_and_convert()
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")