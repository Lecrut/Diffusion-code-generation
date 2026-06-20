import random

def validate_inputs(a, b, c, d):
    if not all(isinstance(x, bool) for x in [a, b, c, d]):
        raise ValueError("All inputs must be boolean values")

def evaluate_expression(a, b, c, d):
    validate_inputs(a, b, c, d)
    return (a and b) or (c and not d)

if __name__ == '__main__':
    for _ in range(100):
        a = random.choice([True, False])
        b = random.choice([True, False])
        c = random.choice([True, False])
        d = random.choice([True, False])
        result = evaluate_expression(a, b, c, d)
        print(f"a={a}, b={b}, c={c}, d={d} -> {result}")