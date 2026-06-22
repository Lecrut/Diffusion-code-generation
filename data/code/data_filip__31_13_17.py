from typing import Union

def hex_to_decimal(hex_input: str) -> int:
    return int(hex_input, 16)

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)
    sample_hex_2 = "FF"
    result_2 = hex_to_decimal(sample_hex_2)
    print(result_2)