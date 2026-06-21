import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def test_expression():
    for _ in range(100):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        expected = (a and b) or (c and not d)
        result = evaluate_expression(a, b, c, d)
        if result != expected:
            raise AssertionError(f"Failed for a={a}, b={b}, c={c}, d={d}: expected {expected}, got {result}")
    return True

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    sample_result = evaluate_expression(sample_a, sample_b, sample_c, sample_d)
    print(sample_result)
    test_passed = test_expression()
    print(test_passed)