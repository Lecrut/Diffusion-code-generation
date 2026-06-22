def is_within_range(number, lower_bound, upper_bound):
    try:
        return lower_bound <= number <= upper_bound
    except TypeError:
        raise ValueError("All inputs must be numeric values.")

if __name__ == '__main__':
    sample_number = 7
    sample_lower_bound = 5
    sample_upper_bound = 10
    result = is_within_range(sample_number, sample_lower_bound, sample_upper_bound)
    print(result)