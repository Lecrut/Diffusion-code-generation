import random

def evaluate_logic(a, b, c, d):
    first_term = a and b
    second_term = c and not d
    result = first_term or second_term
    return result

def run_verification():
    for _ in range(100):
        val_a = random.choice([True, False])
        val_b = random.choice([True, False])
        val_c = random.choice([True, False])
        val_d = random.choice([True, False])
        expected_result = (val_a and val_b) or (val_c and not val_d)
        computed_result = evaluate_logic(val_a, val_b, val_c, val_d)
        if computed_result != expected_result:
            raise AssertionError(
                f"Mismatch for a={val_a}, b={val_b}, c={val_c}, d={val_d}: "
                f"expected {expected_result}, got {computed_result}"
            )

if __name__ == '__main__':
    run_verification()
    sample_a = False
    sample_b = True
    sample_c = True
    sample_d = True
    computed_output = evaluate_logic(sample_a, sample_b, sample_c, sample_d)
    print(computed_output)