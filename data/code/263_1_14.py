def is_within_range(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound

if __name__ == '__main__':
    sample_number = 5
    sample_lower_bound = 1
    sample_upper_bound = 10
    print(is_within_range(sample_number, sample_lower_bound, sample_upper_bound))