def evaluate_conditions(cond1, cond2, cond3, cond4):
    short_circuit_result = (cond1 and cond2) or (cond3 and cond4)
    return short_circuit_result

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    result = evaluate_conditions(sample_a, sample_b, sample_c, sample_d)
    print(f"Sample a: {sample_a}")
    print(f"Sample b: {sample_b}")
    print(f"Sample c: {sample_c}")
    print(f"Sample d: {sample_d}")
    print(f"Result of (a and b) or (c and d): {result}")