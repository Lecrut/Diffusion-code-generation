import sys
def is_strictly_positive(value: float) -> bool:
    epsilon = 1e-9
    return value > epsilon
if __name__ == '__main__':
    test_values = [0.5, -2.3, 1e-7, -1e-8, 0]
    for val in test_values:
        result = is_strictly_positive(val)
        print(f"{val}: {result}")