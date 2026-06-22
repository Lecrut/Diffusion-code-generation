def is_within_range(value, lower_bound, upper_bound):
    if not isinstance(value, (int, float)) or not isinstance(lower_bound, (int, float)) or (not isinstance(upper_bound, (int, float))):
        raise ValueError('All arguments must be numbers.')
    return lower_bound <= value <= upper_bound
if __name__ == '__main__':
    print(is_within_range(5, 1, 10))
    print(is_within_range(0, -5, 5))
    print(is_within_range(15, 10, 20))
    print(is_within_range('a', 1, 10))