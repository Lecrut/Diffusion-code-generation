def xor(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Both inputs must be boolean values.')
    return (a + b) % 2 == 1
if __name__ == '__main__':
    print(xor(True, False))
    print(xor(False, True))
    print(xor(True, True))
    print(xor(False, False))