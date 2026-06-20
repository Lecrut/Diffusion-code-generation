import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    sample_values = [
        (True, False, True, False),
        (False, True, False, True),
        (True, True, False, True),
        (False, False, True, False)
    ]
    for a, b, c, d in sample_values:
        result = evaluate_expression(a, b, c, d)
        print(f"a={a}, b={b}, c={c}, d={d} -> {result}")