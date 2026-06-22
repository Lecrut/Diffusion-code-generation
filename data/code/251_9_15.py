def determine_the_largest_number_present_filter_valid(sample_records):
    valid_numbers = []
    for record in sample_records:
        try:
            number = int(record)
            if number > 0:
                valid_numbers.append(number)
        except ValueError:
            continue
    return max(valid_numbers) if valid_numbers else None

if __name__ == '__main__':
    sample_values = ['123', '456', '-789', 'abc', '0']
    print(determine_the_largest_number_present_filter_valid(sample_values))