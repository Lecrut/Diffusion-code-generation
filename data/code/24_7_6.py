import math
def is_strictly_less_than_zero(x):
    if x < 0:
        return True
    return False
if __name__ == '__main__':
    test_values = [
        -0.000001,
        -1.0,
        0.0,
        1e-10,
        -9.999999999999999,
        0.0,
        -0.0
    ]
    for value in test_values:
        result = is_strictly_less_than_zero(value)
        print(f"Is {value} strictly less than zero? {result}")