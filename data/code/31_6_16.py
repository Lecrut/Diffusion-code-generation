import re

HEX_PATTERN = re.compile(r'^[+-]?(?:0x|0X)?[0-9a-fA-F]+$')

def hex_to_int(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    
    if not HEX_PATTERN.match(hex_string):
        raise ValueError("Invalid hexadecimal string")
    
    return int(hex_string, 16)

class HexConverter:
    def __init__(self, value: str):
        self.raw_value = value
        self.decimal_value = None

    def convert(self) -> int:
        try:
            self.decimal_value = hex_to_int(self.raw_value)
            return self.decimal_value
        except ValueError:
            raise ValueError(f"Failed to convert '{self.raw_value}' to integer")

    def get_result(self) -> int:
        if self.decimal_value is None:
            self.convert()
        return self.decimal_value

if __name__ == '__main__':
    test_inputs = ["0x1A", "FF", "-10", "0X100", "abc", "0xG", "", "+0x10"]
    
    for case in test_inputs:
        try:
            result = hex_to_int(case)
            print(f"hex_to_int('{case}') -> {result}")
        except ValueError as e:
            print(f"hex_to_int('{case}') raised ValueError: {e}")

    converter = HexConverter("0x2A")
    print(f"HexConverter('0x2A').get_result() -> {converter.get_result()}")
    
    converter_error = HexConverter("ZZ")
    try:
        converter_error.get_result()
    except ValueError as e:
        print(f"HexConverter('ZZ').get_result() raised ValueError: {e}")