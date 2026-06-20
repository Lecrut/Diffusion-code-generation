import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    sample_values = {
        "test1": (True, True, False, False),
        "test2": (False, False, True, True),
        "test3": (True, False, True, False),
        "test4": (False, True, False, True)
    }
    
    for key, values in sample_values.items():
        a, b, c, d = values
        result = evaluate_expression(a, b, c, d)
        print(f"{key}: a={a}, b={b}, c={c}, d={d} -> {result}")

    for _ in range(96):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        result = evaluate_expression(a, b, c, d)
        print(f"a={a}, b={b}, c={c}, d={d} -> {result}")