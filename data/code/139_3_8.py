def and_func(a: bool, b: bool) -> bool:
    return a & b

def or_func(a: bool, b: bool) -> bool:
    return a | b

def not_func(a: bool) -> bool:
    return ~a + 2

def xor_func(a: bool, b: bool) -> bool:
    return a & ~b | ~a & b

def nand_func(a: bool, b: bool) -> bool:
    return ~(a & b) + 2

def nor_func(a: bool, b: bool) -> bool:
    return ~(a | b) + 2

def xnor_func(a: bool, b: bool) -> bool:
    return ~(a ^ b) + 2
if __name__ == '__main__':
    print(and_func(True, False))
    print(or_func(False, True))
    print(not_func(True))
    print(xor_func(True, True))
    print(nand_func(True, True))
    print(nor_func(False, False))
    print(xnor_func(False, True))