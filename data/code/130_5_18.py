EPSILON = 1e-9

def is_zero(value: float) -> bool:
    return abs(value) < EPSILON

if __name__ == '__main__':
    test_values = [0.0, EPSILON / 2, -EPSILON / 2, 1e-8, -1e-8]
    results = {val: is_zero(val) for val in test_values}
    print(results)