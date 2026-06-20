def bitwise_and(a: int, b: int) -> int:
    return a & b

def bitwise_or(a: int, b: int) -> int:
    return a | b

def bitwise_not(a: int) -> int:
    return ~a
if __name__ == '__main__':
    print(bitwise_and(5, 3))
    print(bitwise_or(5, 3))
    print(bitwise_not(5))