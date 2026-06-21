from typing import Final

HEX_TABLE: Final[dict[str, int]] = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def hex_to_decimal(hex_string: str) -> int:
    result: int = 0
    for char in hex_string:
        if char not in HEX_TABLE:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        digit_value: int = HEX_TABLE[char]
        result = (result << 4) | digit_value
    return result

if __name__ == '__main__':
    sample_hex: str = "1A3F"
    decimal_value: int = hex_to_decimal(sample_hex)
    print(decimal_value)