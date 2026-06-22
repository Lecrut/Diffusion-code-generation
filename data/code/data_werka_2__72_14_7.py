def count_matching_at_indices(arr1, arr2, index_map):
    count = 0
    for label, pos in index_map.items():
        if pos < len(arr1) and pos < len(arr2):
            if arr1[pos] == arr2[pos]:
                count += 1
    return count

if __name__ == '__main__':
    data_a = [1, 2, 3, 4, 5]
    data_b = [1, 2, 6, 4, 7]
    positions = {
        'head': 0,
        'mid': 2,
        'tail': 4
    }
    result = count_matching_at_indices(data_a, data_b, positions)
    print(result)