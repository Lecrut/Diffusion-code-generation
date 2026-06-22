def determine_the_largest_number_present_filter_valid(data):
    if not data:
        return None
    largest = None
    for number in data:
        if isinstance(number, (int, float)) and (largest is None or number > largest):
            largest = number
    return largest

if __name__ == '__main__':
    mock_data = [45, 12, '89', 3.5, 67, None, 22]
    result = determine_the_largest_number_present_filter_valid(mock_data)
    print(result)