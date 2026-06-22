def validate_logic_inputs(a, b, c):
    valid_types = (bool, int)
    if not all(isinstance(x, valid_types) for x in (a, b, c)):
        raise ValueError("Inputs must be boolean or integer types")
    if not all(x in (0, 1, True, False) for x in (a, b, c)):
        raise ValueError("Inputs must be 0, 1, True, or False")
    return True

def compute_and_gate(a, b, c):
    if not validate_logic_inputs(a, b, c):
        return False
    return a and b and c

if __name__ == '__main__':
    val_a = 1
    val_b = 1
    val_c = 0
    result = compute_and_gate(val_a, val_b, val_c)
    print(result)