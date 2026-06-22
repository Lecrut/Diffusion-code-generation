def is_within_range(value, lower_bound, upper_bound):
    try:
        if lower_bound <= value <= upper_bound:
            return True
        else:
            return False
    except TypeError:
        raise ValueError("All inputs must be numeric values.")

if __name__ == '__main__':
    sample_value = 7
    lower_limit = 5
    upper_limit = 10
    result = is_within_range(sample_value, lower_limit, upper_limit)
    print(result)