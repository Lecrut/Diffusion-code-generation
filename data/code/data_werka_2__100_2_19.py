def validate_inputs(a, b, c):
    if not isinstance(a, (int, bool)):
        raise ValueError("Input a must be an integer or boolean")
    if not isinstance(b, (int, bool)):
        raise ValueError("Input b must be an integer or boolean")
    if not isinstance(c, (int, bool)):
        raise ValueError("Input c must be an integer or boolean")
    return True

def compute_and_gate(a, b, c):
    validate_inputs(a, b, c)
    return a and b and c

if __name__ == '__main__':
    val_a = 1
    val_b = 1
    val_c = 0
    output = compute_and_gate(val_a, val_b, val_c)
    print(output)