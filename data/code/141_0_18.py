def bitwise_and(A: bool, B: bool) -> bool:
    return A & B

def bitwise_or(A: bool, B: bool) -> bool:
    return A | B

def bitwise_not(A: bool) -> bool:
    return not A

if __name__ == '__main__':
    print(bitwise_and(True, False))
    print(bitwise_or(False, True))
    print(bitwise_not(True))