def find_last_greater_equal(data, threshold):
    for index in range(len(data) - 1, -1, -1):
        if data[index] >= threshold:
            return index
    return -1

if __name__ == '__main__':
    sample_list = [7, 12, 8, 15, 3, 9]
    threshold_value = 10
    result_index = find_last_greater_equal(sample_list, threshold_value)
    print(result_index)