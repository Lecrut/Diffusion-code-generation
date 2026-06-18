# Check if x is negative using a concise one-liner expression
result = lambda: True if isinstance(x, (int, float)) else False  # Placeholder logic since we need to check negativity directly without input()
if __name__ == '__main__':
    test_cases = [(-5), (-3.14), 0, (2)]
    for val in test_cases:
        x = val
        is_negative = True if isinstance(x, (int, float)) and x < 0 else False
        print(f"x={val}, Is negative? {is_negative}")