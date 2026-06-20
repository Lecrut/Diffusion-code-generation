def evaluate_logic(a: bool, b: bool, c: bool) -> bool:
    and_result = a and b
    not_c = not c
    return and_result or not_c

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    result = evaluate_logic(sample_a, sample_b, sample_c)
    print(f"Input A: {sample_a}")
    print(f"Input B: {sample_b}")
    print(f"Input C: {sample_c}")
    print(f"Result of (A AND B) OR (NOT C): {result}")

    sample_a = False
    sample_b = True
    sample_c = False
    result = evaluate_logic(sample_a, sample_b, sample_c)
    print(f"Input A: {sample_a}")
    print(f"Input B: {sample_b}")
    print(f"Input C: {sample_c}")
    print(f"Result of (A AND B) OR (NOT C): {result}")