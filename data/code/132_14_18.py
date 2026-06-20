XOR_TABLE = {
    (True, True): False,
    (False, False): False,
    (True, False): True,
    (False, True): True,
}

def xor(a: bool, b: bool) -> bool:
    return XOR_TABLE[(a, b)]

if __name__ == '__main__':
    print(xor(True, False))
    print(xor(False, True))
    print(xor(True, True))
    print(xor(False, False))