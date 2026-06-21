from typing import Final

HEX_INPUT: Final[str] = "1A3F"

def hex_to_decimal(hex_str: str) -> int:
    result: int = 0
    length: int = len(hex_str)
    for i, char in enumerate(hex_str):
        digit: int = int(char, 16)
        power: int = length - 1 - i
        result |= digit << (4 * power)
    return result

if __name__ == '__main__':
    print(hex_to_decimal(HEX_INPUT))