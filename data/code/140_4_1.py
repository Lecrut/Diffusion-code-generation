def is_within_range(target, min_val, max_val):
    return min_val <= target <= max_val
if __name__ == '__main__':
    test_cases = [
        (10, 5, 15),
        (20, 10, 20),
        (3, 1, 2),
        (15, 10, 15),
        (0, -5, 5),
        (100, 0, 50)
    ]
    for target, min_val, max_val in test_cases:
        result = is_within_range(target, min_val, max_val)
        print(f"Target: {target}, Range: [{min_val}, {max_val}] -> Result: {result}")