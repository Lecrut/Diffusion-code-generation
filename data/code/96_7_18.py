import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

def validate_inputs(a, b, c, d):
    if not isinstance(a, bool) or not isinstance(b, bool) or not isinstance(c, bool) or not isinstance(d, bool):
        raise ValueError("All inputs must be boolean values")

if __name__ == '__main__':
    for _ in range(100):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        
        validate_inputs(a, b, c, d)
        
        result = evaluate_expression(a, b, c, d)
        print(f"a={a}, b={b}, c={c}, d={d} -> {result}")