from numbers import Number
def is_positive(value: Number) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [5, -3, 0, 2.5, float('inf'), float('-inf')]
    for val in test_cases:
        result = is_positive(val)
        print(f"is_positive({val}) -> {result}")