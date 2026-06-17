import sys
def is_strictly_positive(value):
    if value > 0:
        return True
    eps = sys.float_info.epsilon * max(1.0, abs(value))
    if value > -eps:
        return True
    return False
if __name__ == '__main__':
    sample_values = [
        0.0,
        -0.00000000000001,
        0.00000000000001,
        float('inf'),
        float('-inf'),
    ]
    for val in sample_values:
        result = is_strictly_positive(val)
        print(f"{val} -> {result}")