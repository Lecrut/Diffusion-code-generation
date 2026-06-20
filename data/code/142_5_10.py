def compare_boolean_values(a: bool, b: bool) -> bool:
    return a == b

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    result = compare_boolean_values(sample_a, sample_b)
    print(f"Sample A: {sample_a}, Sample B: {sample_b}, Result: {result}")