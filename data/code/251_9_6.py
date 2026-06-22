def determine_the_largest_number_present_filter_valid(sample_records):
    valid_numbers = [int(record) for record in sample_records if record.isdigit()]
    return max(valid_numbers)

if __name__ == '__main__':
    sample_values = ['123', 'abc', '456', '789']
    print(determine_the_largest_number_present_filter_valid(sample_values))