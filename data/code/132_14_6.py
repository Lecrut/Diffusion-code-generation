XOR_ZERO = 0
XOR_ONE = 1

def xor(a: bool, b: bool) -> bool:
    return (a + b) % XOR_TWO == XOR_ONE

if __name__ == '__main__':
    print(xor(True, False))
    print(xor(False, True))
    print(xor(True, True))
    print(xor(False, False))