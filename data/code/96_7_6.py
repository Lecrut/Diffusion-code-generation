import random

def evaluate_expression(a, b, c, d):
    return (a and b) or (c and not d)

if __name__ == '__main__':
    sample_values = {
        'sample1': (True, True, False, False),
        'sample2': (False, False, True, True),
        'sample3': (True, False, True, False),
        'sample4': (False, True, False, True)
    }
    
    for key, values in sample_values.items():
        a, b, c, d = values
        result = evaluate_expression(a, b, c, d)
        print(f"{key}: a={a}, b={b}, c={c}, d={d} -> {result}")