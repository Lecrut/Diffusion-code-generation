import math
def manipulate_ratio(a, b):
    initial_ratio = a / b
    ratio_halved = initial_ratio / 2
    ratio_doubled = initial_ratio * 2
    if a != 0:
        ratio_inverted = b / a
    else:
        ratio_inverted = float('inf')
    return {
        "initial_ratio": initial_ratio,
        "halved_ratio": ratio_halved,
        "doubled_ratio": ratio_doubled,
        "inverted_ratio": ratio_inverted
    }
if __name__ == '__main__':
    a_val = 10
    b_val = 4
    results = manipulate_ratio(a_val, b_val)
    print(f"Initial numbers: a = {a_val}, b = {b_val}")
    print("--- Ratio Manipulation ---")
    print(f"Initial ratio (a:b): {a_val}: {b_val} or {results['initial_ratio']:.4f}")
    print(f"Ratio halved (a/2 : b): {a_val/2}: {b_val} or {results['halved_ratio']:.4f}")
    print(f"Ratio doubled (2a : b): {2*a_val}: {b_val} or {results['doubled_ratio']:.4f}")
    print(f"Ratio inverted (b:a): {b_val}: {a_val} or {results['inverted_ratio']:.4f}")