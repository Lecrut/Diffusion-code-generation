def find_last_index_greater_or_equal(lst, threshold):
    index = -1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] >= threshold:
            index = i
            break
    return index

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    threshold_value = 45
    result = find_last_index_greater_or_equal(sample_list, threshold_value)
    print(result)