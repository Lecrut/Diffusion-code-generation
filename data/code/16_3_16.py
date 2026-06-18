# Expression to check if x is positive: bool(x > 0)
if __name__ == '__main__':
    # Test cases without user input or external dependencies
    test_values = [5, -3, 0]
    for val in test_values:
        print(f"Testing {val}: {bool(val > 0)}")