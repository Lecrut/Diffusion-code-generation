import math
def is_positive(value):
    return value > 0.0
if __name__ == '__main__':
    test_values = [1.0, 0.0, -3.14, 0.0000000000000001, -0.0000000000000001]
    for val in test_values:
        result = is_positive(val)
        print(f"Is {val} positive? {result}")