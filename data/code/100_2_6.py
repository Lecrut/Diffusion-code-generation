def _validate_inputs(a, b, c):
    if not isinstance(a, bool):
        raise ValueError("Input a must be a boolean")
    if not isinstance(b, bool):
        raise ValueError("Input b must be a boolean")
    if not isinstance(c, bool):
        raise ValueError("Input c must be a boolean")
    return True

def evaluate_three_input_and(a, b, c):
    _validate_inputs(a, b, c)
    return a and b and c

if __name__ == '__main__':
    val_a = True
    val_b = False
    val_c = True
    output = evaluate_three_input_and(val_a, val_b, val_c)
    print(output)