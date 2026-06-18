def is_zero(value):
    """Returns True if value is zero, False otherwise."""
    return value == 0

if __name__ == '__main__':
    test_cases = [0, -15789234.67, float('inf'), float('-inf')]
    
    for case in test_cases:
        result = is_zero(case)
        print(f"is_zero({case}) -> {result}")