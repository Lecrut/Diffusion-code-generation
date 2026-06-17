def find_adjacent_differences(arr):
    if len(arr) < 2:
        return []
    differences = []
    for i in range(len(arr) - 1):
        diff = abs(arr[i+1] - arr[i])
        differences.append(diff)
    return differences
if __name__ == '__main__':
    sample_array_1 = [1, 3, 5, 2, 8]
    result_1 = find_adjacent_differences(sample_array_1)
    print(result_1)
    sample_array_2 = [10, 7, 4, 1, 9]
    result_2 = find_adjacent_differences(sample_array_2)
    print(result_2)
    sample_array_3 = [5, 5, 5, 5]
    result_3 = find_adjacent_differences(sample_array_3)
    print(result_3)
    sample_array_4 = [100]
    result_4 = find_adjacent_differences(sample_array_4)
    print(result_4)