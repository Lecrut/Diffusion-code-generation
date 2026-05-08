def test_multiple_conditions(a: bool, b: bool, c: bool) -> bool:
    return a and b and c
if __name__ == '__main__':
    condition_a = True
    condition_b = False
    condition_c = True
    result = test_multiple_conditions(condition_a, condition_b, condition_c)
    print(f"Condition A: {condition_a}")
    print(f"Condition B: {condition_b}")
    print(f"Condition C: {condition_c}")
    print(f"Result of simultaneous test: {result}")
    condition_a_true = True
    condition_b_true = True
    condition_c_true = True
    result_all_true = test_multiple_conditions(condition_a_true, condition_b_true, condition_c_true)
    print(f"\nResult when all are True: {result_all_true}")