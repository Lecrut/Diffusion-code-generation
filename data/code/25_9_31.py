def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_values = [0, 1, -1, 0.0, -0.0, 1e-10, float('inf'), float('-inf')]
    for val in test_values:
        print(f"is_zero({val}) -> {is_zero(val)}")