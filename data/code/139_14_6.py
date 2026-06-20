def validate_input(a: bool, b: bool) -> None:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean values.')

def AND(a: bool, b: bool) -> bool:
    validate_input(a, b)
    return a and b

def OR(a: bool, b: bool) -> bool:
    validate_input(a, b)
    return a or b

def NOT(a: bool) -> bool:
    validate_input(a, None)
    return not a

def XOR(a: bool, b: bool) -> bool:
    validate_input(a, b)
    return a and (not b) or (not a and b)

def NAND(a: bool, b: bool) -> bool:
    validate_input(a, b)
    return not AND(a, b)

def NOR(a: bool, b: bool) -> bool:
    validate_input(a, b)
    return not OR(a, b)
if __name__ == '__main__':
    print(AND(True, False))
    print(OR(False, True))
    print(NOT(True))
    print(XOR(True, True))
    print(NAND(True, True))