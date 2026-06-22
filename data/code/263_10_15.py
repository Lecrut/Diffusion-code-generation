def is_number_in_range(number, range_min, range_max):
    return range_min <= number <= range_max

if __name__ == '__main__':
    sample_number = 7
    sample_min = 5
    sample_max = 10
    print(is_number_in_range(sample_number, sample_min, sample_max))