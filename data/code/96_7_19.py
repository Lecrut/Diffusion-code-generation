import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    test_cases = {
        'case1': (True, True, False, False),
        'case2': (False, False, True, True),
        'case3': (True, False, True, False),
        'case4': (False, True, False, True)
    }
    
    for case_name, (a, b, c, d) in test_cases.items():
        result = evaluate_expression(a, b, c, d)
        print(f"{case_name}: a={a}, b={b}, c={c}, d={d} -> {result}")
    
    for _ in range(96):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        result = evaluate_expression(a, b, c, d)
        print(f"a={a}, b={b}, c={c}, d={d} -> {result}")