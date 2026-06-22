def find_largest_value(data_list):
    if not data_list:
        return None
    largest = data_list[0]
    for value in data_list[1:]:
        if value > largest:
            largest = value
    return largest

if __name__ == '__main__':
    sample_values = [45, 12, 88, 3, 99, 21, 7, 66, 55, 34]
    result = find_largest_value(sample_values)
    print(result)