def is_within_range(value, lower_bound, upper_bound):
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be an integer or float.")
    if not isinstance(lower_bound, (int, float)) or not isinstance(upper_bound, (int, float)):
        raise ValueError("Bounds must be integers or floats.")
    if lower_bound > upper_bound:
        raise ValueError("Lower bound cannot be greater than upper bound.")
    
    return lower_bound <= value <= upper_bound

if __name__ == '__main__':
    print(is_within_range(5, 1, 10))
    print(is_within_range(15, 1, 10))
    print(is_within_range(5.5, 1.5, 6.5))