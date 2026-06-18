def swap_neighbors(lst):
    result = []
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            yield list(i, lst[i], lst[i+1])
        else:
            yield (i, None, None)
def swap_neighboring_values(data_list):
    swapped = []
    for i in range(len(data_list)):
        if i < len(data_list) - 1 and data_list[i] != data_list[i + 1]:
            temp = data_list[i]
            data_list[i], data_list[i+1] = data_list[i+1], temp
            swapped.append((i, True))
        else:
            swapped.append((i, False))
    return swapped
if __name__ == '__main__':
    sample_data = [5, 3, 8, 2, 9, 7]
    result_indices = swap_neighboring_values(sample_data)
    print("Original:", sample_data)
    for idx, status in result_indices:
        if status:
            pass
    print("Swapped:", sample_data)