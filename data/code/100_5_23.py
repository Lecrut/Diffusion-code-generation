def validate_boolean(value):
    if type(value) is not bool:
        raise ValueError("Input must be a boolean")
    return True

def compute_and_logic(input_a, input_b):
    validate_boolean(input_a)
    validate_boolean(input_b)
    return input_a and input_b

if __name__ == '__main__':
    val_a = True
    val_b = False
    output = compute_and_logic(val_a, val_b)
    print(output)