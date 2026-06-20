def boolean_xnor(a: bool, b: bool) -> bool:
    return a == b
if __name__ == '__main__':
    print(boolean_xnor(True, True))
    print(boolean_xnor(False, False))
    print(boolean_xnor(True, False))
    print(boolean_xnor(False, True))