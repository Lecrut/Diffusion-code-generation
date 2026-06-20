def evaluate_and_condition(a, b):
    if isinstance(a, bool) and isinstance(b, bool):
        return a and b
    else:
        raise ValueError("Inputs must be booleans")

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = evaluate_and_condition(sample_a, sample_b)
    print(result)