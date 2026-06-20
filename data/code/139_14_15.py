def and_gate(a: bool, b: bool) -> bool:
    return a and b

def or_gate(a: bool, b: bool) -> bool:
    return a or b

def not_gate(a: bool) -> bool:
    return not a

def xor_gate(a: bool, b: bool) -> bool:
    return a and (not b) or (not a and b)

def nand_gate(a: bool, b: bool) -> bool:
    return not (a and b)

def nor_gate(a: bool, b: bool) -> bool:
    return not (a or b)
if __name__ == '__main__':
    print(and_gate(True, False))
    print(or_gate(False, True))
    print(not_gate(True))
    print(xor_gate(True, True))
    print(nand_gate(False, False))
    print(nor_gate(True, True))