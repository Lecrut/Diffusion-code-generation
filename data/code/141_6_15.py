def validate_inputs(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers.")

def bitwise_operations(a, b):
    validate_inputs(a, b)
    return a & b, a | b, ~a

if __name__ == '__main__':
    result_and, result_or, result_not = bitwise_operations(5, 3)
    print(f"AND: {result_and}, OR: {result_or}, NOT: {result_not}")