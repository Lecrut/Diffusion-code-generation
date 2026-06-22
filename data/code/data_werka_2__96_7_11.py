import random

NUM_TESTS = 100

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def run_validation():
    for _ in range(NUM_TESTS):
        inputs = [random.choice([True, False]) for _ in range(4)]
        a, b, c, d = inputs
        expected = (a and b) or (c and not d)
        actual = evaluate_expression(a, b, c, d)
        if expected != actual:
            raise AssertionError(f"Validation failed for {inputs}")

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    result = evaluate_expression(sample_a, sample_b, sample_c, sample_d)
    print(result)
    run_validation()
    print(evaluate_expression(True, True, False, True))