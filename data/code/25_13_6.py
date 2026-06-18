def is_zero(x):
    return x == 0

if __name__ == '__main__':
    test_cases = [0, -1, 42]
    for val in test_cases:
        result = is_zero(val)
        print(f"is_zero({val}) = {result}")