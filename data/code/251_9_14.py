def determine_the_largest_number_present_filter_valid(sample_records):
    valid_numbers = [record for record in sample_records if isinstance(record, int) and record > 0]
    return max(valid_numbers)

if __name__ == '__main__':
    sample_values = [10, -2, '3', 5, 0, 7, None, 15]
    print(determine_the_largest_number_present_filter_valid(sample_values))