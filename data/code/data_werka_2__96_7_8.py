import random

def evaluate_expression(a, b, c, d):
    if not all(isinstance(val, bool) for val in (a, b, c, d)):
        raise ValueError("All inputs must be boolean")
    return (a and b) or (c and not d)

def run_validation():
    test_count = 0
    for _ in range(100):
        inputs = [random.choice([True, False]) for _ in range(4)]
        expected = (inputs[0] and inputs[1]) or (inputs[2] and not inputs[3])
        actual = evaluate_expression(*inputs)
        if expected != actual:
            raise AssertionError(f"Mismatch: {inputs} expected {expected} got {actual}")
        test_count += 1
    return test_count

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    result = evaluate_expression(sample_a, sample_b, sample_c, sample_d)
    print(result)
    count = run_validation()
    print(count)