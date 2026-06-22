def is_number_in_range(value, lower_bound, upper_bound):
    if not all(isinstance(x, (int, float)) for x in [value, lower_bound, upper_bound]):
        raise ValueError("All inputs must be numbers.")
    return lower_bound <= value <= upper_bound

if __name__ == '__main__':
    print(is_number_in_range(5, 1, 10))
    print(is_number_in_range(0, -5, 5))
    try:
        print(is_number_in_range('a', 1, 10))
    except ValueError as e:
        print(e)