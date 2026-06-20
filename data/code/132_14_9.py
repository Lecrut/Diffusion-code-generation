XOR_CONST = 1

def xor(a: bool, b: bool) -> bool:
    return (a + b) % XOR_CONST == 1
if __name__ == '__main__':
    print(xor(True, False))
    print(xor(False, True))
    print(xor(True, True))
    print(xor(False, False))