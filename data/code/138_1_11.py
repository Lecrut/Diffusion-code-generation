def validate_inputs(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError('Inputs must be boolean')

def nand_gate(a, b):
    validate_inputs(a, b)
    return not (a and b)
if __name__ == '__main__':
    print(nand_gate(True, True))
    print(nand_gate(True, False))
    print(nand_gate(False, True))
    print(nand_gate(False, False))