from numbers import Number
def is_positive(value: Number) -> bool:
    return value > 0
if __name__ == '__main__':
    test_values = [1, -5, 0, 3.14, float('-inf'), float('inf')]
    for val in test_values:
        print(f"{val}: {is_positive(val)}")