def determine_the_largest_number_present_filter_valid(sample_records):
    valid_numbers = [record for record in sample_records if isinstance(record, (int, float)) and record >= 0]
    return max(valid_numbers) if valid_numbers else None

if __name__ == '__main__':
    sample_values = [10, -5, 'a', 3.14, 20, None, 0]
    print(determine_the_largest_number_present_filter_valid(sample_values))