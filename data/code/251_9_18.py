def determine_the_largest_number_present_filter_valid(data):
    valid_numbers = [x for x in data if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return max(valid_numbers) if valid_numbers else None

if __name__ == '__main__':
    mock_data = [45, 12, '89', True, 3.14, 67, False, 22]
    result = determine_the_largest_number_present_filter_valid(mock_data)
    print(result)