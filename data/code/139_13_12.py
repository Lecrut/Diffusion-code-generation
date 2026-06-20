def AND(a: int, b: int) -> int:
    return a & b

def OR(a: int, b: int) -> int:
    return a | b

def XOR(a: int, b: int) -> int:
    return a ^ b

def NOT(a: int) -> int:
    return ~a + 1
if __name__ == '__main__':
    print(AND(1, 0))
    print(OR(1, 0))
    print(XOR(1, 0))
    print(NOT(1))