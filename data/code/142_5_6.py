def check_same_truth_value(a: bool, b: bool) -> bool:
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values.")
    return a == b

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = check_same_truth_value(sample_a, sample_b)
    print(f"Sample A: {sample_a}, Sample B: {sample_b}")
    print(f"Do they have the same truth value? {result}")