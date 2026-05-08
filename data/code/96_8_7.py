import random
def evaluate_expression(a, b, c, d):
    result = (a and b) or (c and not d)
    return result
def test_expression():
    num_tests = 100
    for _ in range(num_tests):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        expected = evaluate_expression(a, b, c, d)
        actual = evaluate_expression(a, b, c, d)
        if actual != expected:
            print(f"Test failed for a={a}, b={b}, c={c}, d={d}. Expected: {expected}, Got: {actual}")
            return
    print("All 100 tests passed.")
if __name__ == '__main__':
    test_expression()