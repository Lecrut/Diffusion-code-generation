def bitwise_and(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean')
    return a & b

def bitwise_or(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean')
    return a | b

def bitwise_not(a: bool) -> bool:
    if not isinstance(a, bool):
        raise ValueError('Input must be boolean')
    return not a

if __name__ == '__main__':
    print(bitwise_and(True, False))
    print(bitwise_or(False, True))
    print(bitwise_not(True))