def get_middle_value(data):
    if not data:
        return None
    sorted_data = sorted(data)
    length = len(sorted_data)
    if length % 2 == 0:
        mid_index = length // 2
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
    mid_index = length // 2
    return sorted_data[mid_index]

if __name__ == '__main__':
    sample_list = [7, 3, 9, 1, 5]
    result = get_middle_value(sample_list)
    print(result)