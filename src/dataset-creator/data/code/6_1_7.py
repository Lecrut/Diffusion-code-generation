import math
def is_greater(a: float, b: float) -> bool:
    if not (math.isnan(b)):
        return a > b
    else:
        return False
if __name__ == '__main__':
    test_cases = [
        (5.0, 3.0),
        (float('nan'), 2.0),
        (1.0, float('nan')),
        (-5.0, -7.0),
        (float('inf'), float('-inf'))
    ]
    for val_a, val_b in test_cases:
        result = is_greater(val_a, val_b)
        print(f"is_greater({val_a}, {val_b}) = {result}")