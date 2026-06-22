def get_median_element(data):
    if not data:
        raise ValueError("List cannot be empty")
    sorted_data = sorted(data)
    length = len(sorted_data)
    if length % 2 == 1:
        return sorted_data[length // 2]
    else:
        mid_right = length // 2
        mid_left = mid_right - 1
        return (sorted_data[mid_left] + sorted_data[mid_right]) / 2

if __name__ == '__main__':
    sample_list = [7, 1, 3, 9, 5, 2, 8, 4, 6]
    result = get_median_element(sample_list)
    print(result)