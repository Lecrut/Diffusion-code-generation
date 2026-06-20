def xnor(a: bool, b: bool) -> bool:
    return not a ^ b
if __name__ == '__main__':
    print(xnor(True, True))
    print(xnor(False, False))
    print(xnor(True, False))
    print(xnor(False, True))