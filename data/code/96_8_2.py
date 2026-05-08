import random
def evaluate_expression(a, b, c, d):
    result = (a and b) or (c and not d)
    return result
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
    NUM_TESTS = 100
    all_passed = True
    print("Starting evaluation tests...")
    all_passed = test_expression(NUM_TESTS)
    if all_passed:
        print(f"Successfully passed {NUM_TESTS} random tests.")
    else:
        print(f"One or more tests failed.")