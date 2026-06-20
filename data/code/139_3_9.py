def bitwise_and(a: int, b: int) -> int:
    return a & b

def bitwise_or(a: int, b: int) -> int:
    return a | b

def bitwise_not(a: int) -> int:
    return ~a

def bitwise_xor(a: int, b: int) -> int:
    return a ^ b

def bitwise_nand(a: int, b: int) -> int:
    return ~(a & b)

def bitwise_nor(a: int, b: int) -> int:
    return ~(a | b)

def bitwise_xnor(a: int, b: int) -> int:
    return ~(a ^ b)
if __name__ == '__main__':
    print(bitwise_and(5, 3))
    print(bitwise_or(5, 3))
    print(bitwise_not(5))
    print(bitwise_xor(5, 3))
    print(bitwise_nand(5, 3))
    print(bitwise_nor(5, 3))
    print(bitwise_xnor(5, 3))