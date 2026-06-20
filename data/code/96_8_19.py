def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def test_expression(num_tests):
    for _ in range(num_tests):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        expected = evaluate_expression(a, b, c, d)
        actual = evaluate_expression(a, b, c, d)
        if expected != actual:
            print(f"Test failed for a={a}, b={b}, c={c}, d={d}. Expected: {expected}, Got: {actual}")
            return False
    return True

if __name__ == '__main__':
    import random
    NUM_TESTS = 100
    if not test_expression(NUM_TESTS):
        print("Some tests failed.")
    else:
        print("All tests passed.")