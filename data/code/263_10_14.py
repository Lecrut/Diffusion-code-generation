def is_within_range(value, lower_bound, upper_bound):
    if not (isinstance(lower_bound, (int, float)) and isinstance(upper_bound, (int, float))):
        raise ValueError('Lower and upper bounds must be numeric values.')
    if not isinstance(value, (int, float)):
        raise ValueError('Value to check must be a numeric value.')
    return lower_bound <= value <= upper_bound
if __name__ == '__main__':
    test_value = 7
    lower_limit = 5
    upper_limit = 10
    result = is_within_range(test_value, lower_limit, upper_limit)
    print(result)