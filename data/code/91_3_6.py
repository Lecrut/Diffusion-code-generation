from typing import Final

BOOL_TRUE_BIT: Final[int] = 1
BOOL_FALSE_BIT: Final[int] = 0

def invert_boolean(value: bool) -> bool:
    int_val: int = 1 if value else 0
    inverted_int: int = int_val ^ BOOL_TRUE_BIT
    return bool(inverted_int)

if __name__ == '__main__':
    print(invert_boolean(True))
    print(invert_boolean(False))