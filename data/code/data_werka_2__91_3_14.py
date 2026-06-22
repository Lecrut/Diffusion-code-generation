from typing import Final

TRUE_BIT: Final[int] = 1
FALSE_BIT: Final[int] = 0

def flip_boolean(value: bool) -> bool:
    bit_value: int = 1 if value else 0
    flipped_bit: int = bit_value ^ TRUE_BIT
    return bool(flipped_bit)

if __name__ == '__main__':
    print(flip_boolean(True))
    print(flip_boolean(False))