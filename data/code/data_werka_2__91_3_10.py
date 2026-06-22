from typing import Final

TRUE_BIT: Final[int] = 1
FALSE_BIT: Final[int] = 0
BIT_MASK: Final[int] = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

def invert_boolean(value: bool) -> bool:
    int_value: int = TRUE_BIT if value else FALSE_BIT
    inverted_int: int = (~int_value) & BIT_MASK
    return bool(inverted_int & TRUE_BIT)

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))