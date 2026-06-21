def validate_and_compute_logic(input_a, input_b):
    if not isinstance(input_a, bool):
        raise ValueError("First input must be a boolean")
    if not isinstance(input_b, bool):
        raise ValueError("Second input must be a boolean")
    return input_a and input_b

def run_sample_logic():
    val_a = True
    val_b = True
    result = validate_and_compute_logic(val_a, val_b)
    print(result)

if __name__ == '__main__':
    run_sample_logic()