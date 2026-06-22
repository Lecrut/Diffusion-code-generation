def is_number_in_range(number, range_min, range_max):
    return range_min <= number <= range_max

if __name__ == '__main__':
    sample_number = 10
    sample_range_min = 5
    sample_range_max = 15
    print(is_number_in_range(sample_number, sample_range_min, sample_range_max))