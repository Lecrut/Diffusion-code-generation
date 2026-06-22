def validate_input(a: int, b: int, c: int) -> bool:
    _MIN = 1
    _MAX = 100
    _MASK = 0x1
    _VALID_MASK = 0xFFFFFFFE

    if not (a & _MASK) == 0:
        raise ValueError(f"a must be even: {a}")
    if not (b & _MASK) == 0:
        raise ValueError(f"b must be even: {b}")
    if not (c & _MASK) == 0:
        raise ValueError(f"c must be even: {c}")

    if a <= _MIN:
        raise ValueError(f"a must be positive: {a}")
    if b <= _MIN:
        raise ValueError(f"b must be positive: {b}")
    if c <= _MIN:
        raise ValueError(f"c must be positive: {c}")

    if a >= _MAX:
        raise ValueError(f"a must be less than 100: {a}")
    if b >= _MAX:
        raise ValueError(f"b must be less than 100: {b}")
    if c >= _MAX:
        raise ValueError(f"c must be less than 100: {c}")

    return True

if __name__ == '__main__':
    try:
        val_a = 2
        val_b = 4
        val_c = 6
        result = validate_input(val_a, val_b, val_c)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        val_a = 0
        val_b = 4
        val_c = 6
        result = validate_input(val_a, val_b, val_c)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        val_a = 2
        val_b = 3
        val_c = 6
        result = validate_input(val_a, val_b, val_c)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    try:
        val_a = 2
        val_b = 4
        val_c = 100
        result = validate_input(val_a, val_b, val_c)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")