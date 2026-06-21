def is_zero(value):
    return value == 0

if __name__ == '__main__':
    test_cases = [0, -0.0, 1e-308, 1e-150, 2.0, 0.0]
    for case in test_cases:
        result = is_zero(case)
        print(f"is_zero({case}) => {result}")