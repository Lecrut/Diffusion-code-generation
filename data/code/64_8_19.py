def find_last_index_greater_or_equal(lst, threshold):
    index = -1
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] >= threshold:
            index = i
            break
    return index

if __name__ == '__main__':
    sample_list = [3, 5, 7, 2, 8, 6, 9]
    threshold_value = 6
    result = find_last_index_greater_or_equal(sample_list, threshold_value)
    print(result)