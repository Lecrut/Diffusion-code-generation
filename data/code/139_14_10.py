from typing import Union

def validate_inputs(a: bool, b: bool = None) -> None:
    if not isinstance(a, bool) or (b is not None and not isinstance(b, bool)):
        raise ValueError("Inputs must be boolean values")

def AND(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return a and b

def OR(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return a or b

def NOT(a: bool) -> bool:
    validate_inputs(a)
    return not a

def XOR(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return a != b

def NAND(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return not (a and b)

def NOR(a: bool, b: bool) -> bool:
    validate_inputs(a, b)
    return not (a or b)

if __name__ == '__main__':
    print(AND(True, False))
    print(OR(False, True))
    print(NOT(True))
    print(XOR(True, True))
    print(NAND(True, True))