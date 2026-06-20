def AND(a: bool, b: bool) -> bool:
    return a & b

def OR(a: bool, b: bool) -> bool:
    return a | b

def NOT(a: bool) -> bool:
    return not a

def XOR(a: bool, b: bool) -> bool:
    return a ^ b
if __name__ == '__main__':
    print(AND(True, False))
    print(OR(False, True))
    print(NOT(True))
    print(XOR(True, True))