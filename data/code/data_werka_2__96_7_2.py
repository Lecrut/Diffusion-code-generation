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
        actual = evaluate_expression(a, b, c, d)
        if expected != actual:
            raise AssertionError(f"Mismatch for a={a}, b={b}, c={c}, d={d}: expected {expected}, got {actual}")
    return True

if __name__ == '__main__':
    sample_result = evaluate_expression(True, False, True, False)
    print(sample_result)
    test_passed = test_expression()
    print(test_passed)