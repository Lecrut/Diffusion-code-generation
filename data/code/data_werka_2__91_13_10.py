def negate_boolean(value: bool) -> bool:
    _BIT_MAP = {
        True: 0,
        False: 1
    }
    _INVERSE_MAP = {
        0: False,
        1: True
    }
    bit = _BIT_MAP[value]
    flipped = bit ^ 1
    return _INVERSE_MAP[flipped]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))