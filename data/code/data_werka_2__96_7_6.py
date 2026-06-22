import random

def _validate_boolean(value, name):
    if not isinstance(value, bool):
        raise ValueError(f"{name} must be a boolean, got {type(value).__name__}")
    return value

def evaluate_logic(a, b, c, d):
    a_val = _validate_boolean(a, "a")
    b_val = _validate_boolean(b, "b")
    c_val = _validate_boolean(c, "c")
    d_val = _validate_boolean(d, "d")
    return (a_val and b_val) or (c_val and not d_val)

def run_verification():
    passed = 0
    for _ in range(100):
        inputs = [random.choice([True, False]) for _ in range(4)]
        a, b, c, d = inputs
        expected = (a and b) or (c and not d)
        result = evaluate_logic(a, b, c, d)
        if result != expected:
            raise AssertionError(f"Test failed for inputs {inputs}")
        passed += 1
    return passed

if __name__ == '__main__':
    sample_a = True
    sample_b = False
    sample_c = True
    sample_d = False
    sample_result = evaluate_logic(sample_a, sample_b, sample_c, sample_d)
    print(sample_result)
    test_count = run_verification()
    print(test_count)