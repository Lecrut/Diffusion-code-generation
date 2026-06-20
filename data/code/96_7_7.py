import random

def evaluate_expression(a, b, c, d):
    if not all(isinstance(x, bool) for x in [a, b, c, d]):
        raise ValueError("All inputs must be boolean values.")
    return (a and b) or (c and not d)

if __name__ == '__main__':
    sample_values = [
        (True, True, False, False),
        (False, False, True, True),
        (True, False, True, False),
        (False, True, False, True)
    ]
    for a, b, c, d in sample_values:
        try:
            result = evaluate_expression(a, b, c, d)
            print(f"a={a}, b={b}, c={c}, d={d} -> {result}")
        except ValueError as e:
            print(e)