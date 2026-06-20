def evaluate_booleans(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be booleans.")
    return a and b

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = evaluate_booleans(sample_a, sample_b)
    print(result)