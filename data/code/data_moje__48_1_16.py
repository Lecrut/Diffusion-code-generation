def get_largest_value(data):
    filtered_data = [item for item in data if isinstance(item, int)]
    if not filtered_data:
        return None
    current_max = filtered_data[0]
    for value in filtered_data[1:]:
        if value > current_max:
            current_max = value
    return current_max

if __name__ == '__main__':
    sample_data = [14, 88, 32, 9, 67, 55, 1, 73, 29, 45]
    largest_int = get_largest_value(sample_data)
    print(largest_int)