def is_valid_number(number):
    return isinstance(number, (int, float)) and not isinstance(number, bool)

def determine_the_largest_number_present_filter_valid(data):
    if not data:
        return None
    valid_data = [num for num in data if is_valid_number(num)]
    if not valid_data:
        return None
    largest = max(valid_data)
    return largest

if __name__ == '__main__':
    mock_data = [45, 12, "89", 3.5, True, 67, None, 22]
    result = determine_the_largest_number_present_filter_valid(mock_data)
    print(result)