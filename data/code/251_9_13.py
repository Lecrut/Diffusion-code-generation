def determine_the_largest_number_present_filter_valid(sample_records):
    valid_numbers = [record for record in sample_records if isinstance(record, (int, float)) and record >= 0]
    return max(valid_numbers) if valid_numbers else None

if __name__ == '__main__':
    sample_values = [10, -5, 3.14, 'a', 20, 0, None, 15.5]
    print(determine_the_largest_number_present_filter_valid(sample_values))