def find_median(data):
    n = len(data)
    if n == 0:
        return None
    sorted_data = sorted(data)
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_data[middle_index]
    else:
        right_middle_index = n // 2
        left_middle_index = right_middle_index - 1
        median = (sorted_data[left_middle_index] + sorted_data[right_middle_index]) / 2
        return median
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    median_value = find_median(sample_list)
    print(median_value)