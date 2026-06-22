def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative.")

def compute_sum():
    a = 15
    b = 27
    validate_inputs(a, b)
    return a + b

if __name__ == '__main__':
    result = compute_sum()
    print(result)