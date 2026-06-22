UNIT = 1

def compute_comparison(length_a, length_b):
    if length_a > length_b:
        gap = length_a - length_b
        return f"Length A is longer than Length B by {gap} units"
    elif length_b > length_a:
        gap = length_b - length_a
        return f"Length B is longer than Length A by {gap} units"
    return "Length A and Length B are equal"

if __name__ == '__main__':
    val_a = 20.0
    val_b = 12.0
    output = compute_comparison(val_a, val_b)
    print(output)