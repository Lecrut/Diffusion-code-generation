def xor(a: bool, b: bool) -> bool:
    return (a + b) % 2 == 1
if __name__ == '__main__':
    print(xor(True, False))
    print(xor(False, True))
    print(xor(True, True))
    print(xor(False, False))