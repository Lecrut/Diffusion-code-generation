def validate_boolean_inputs(val1, val2):
    if type(val1) is not bool or type(val2) is not bool:
        raise ValueError("Inputs must be boolean")
    return True

def compute_and_output(a, b):
    return a and b

def check_logic_consistency(input_a, input_b):
    validate_boolean_inputs(input_a, input_b)
    return compute_and_output(input_a, input_b)

if __name__ == '__main__':
    val_a = True
    val_b = False
    output = check_logic_consistency(val_a, val_b)
    print(output)