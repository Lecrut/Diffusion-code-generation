import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def run_validation():
    test_cases = []
    for _ in range(100):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        test_cases.append((a, b, c, d))
    
    for a, b, c, d in test_cases:
        expected = (a and b) or (c and not d)
        result = evaluate_expression(a, b, c, d)
        if result != expected:
            raise AssertionError(f"Validation failed for inputs a={a}, b={b}, c={c}, d={d}")
    return True

if __name__ == '__main__':
    input_map = {
        "case1": (True, False, True, False),
        "case2": (False, True, False, True),
        "case3": (True, True, False, False)
    }
    
    for key, args in input_map.items():
        val = evaluate_expression(*args)
        print(val)
    
    run_validation()