def find_adjacent_greater_pairs(arr):
    indices = []
    for current_index in range(len(arr) - 1):
        next_index = current_index + 1
        if arr[next_index] > arr[current_index]:
            indices.append(current_index)
    return indices

if __name__ == '__main__':
    sample_array = [1, 3, 2, 4, 5, 7, 6]
    result_indices = find_adjacent_greater_pairs(sample_array)
    print(result_indices)