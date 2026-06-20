def xnor(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values.")
    return a == b

if __name__ == '__main__':
    print(xnor(True, True))
    print(xnor(False, False))
    print(xnor(True, False))
    print(xnor(False, True))