def AND(a: int, b: int) -> int:
    return a & b

def OR(a: int, b: int) -> int:
    return a | b

def XOR(a: int, b: int) -> int:
    return a ^ b

def NOT(a: int) -> int:
    return ~a + 1
if __name__ == '__main__':
    print(AND(3, 5))
    print(OR(3, 5))
    print(XOR(3, 5))
    print(NOT(3))