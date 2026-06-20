def xor(a: bool, b: bool) -> bool:
    return int(a != b)
if __name__ == '__main__':
    print(xor(True, False))
    print(xor(False, True))
    print(xor(True, True))
    print(xor(False, False))