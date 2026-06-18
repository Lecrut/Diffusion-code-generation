import math

def is_zero(x):
    # Treat very small floating-point numbers as zero to avoid edge cases
    return abs(float(x)) < 1e-9 if not isinstance(x, int) else x == 0

if __name__ == '__main__':
    test_cases = [0, -5.234678, 2/3, float(0)]
    for val in test_cases:
        print(f"is_zero({val}) evaluates to {is_zero(val)}")