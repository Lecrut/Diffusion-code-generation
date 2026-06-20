import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    test_cases = {
        1: (True, True, False, False),
        2: (False, False, True, True),
        3: (True, False, True, False),
        4: (False, True, False, True)
    }
    
    for i in range(5):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        result = evaluate_expression(a, b, c, d)
        print(f"a={a}, b={b}, c={c}, d={d} -> {result}")
    
    for case_id, (a, b, c, d) in test_cases.items():
        result = evaluate_expression(a, b, c, d)
        print(f"Test case {case_id}: a={a}, b={b}, c={c}, d={d} -> {result}")