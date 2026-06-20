def AND(a: int, b: int) -> int:
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Inputs must be integers')
    return a & b

def OR(a: int, b: int) -> int:
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Inputs must be integers')
    return a | b

def NOT(a: int) -> int:
    if not isinstance(a, int):
        raise ValueError('Input must be an integer')
    return ~a

def XOR(a: int, b: int) -> int:
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('Inputs must be integers')
    return a ^ b
if __name__ == '__main__':
    print(AND(1, 0))
    print(OR(1, 0))
    print(NOT(1))
    print(XOR(1, 0))