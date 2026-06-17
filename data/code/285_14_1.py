def find_adjacent_differences(arr):
    if len(arr) < 2:
        return []
    differences = []
    for i in range(len(arr) - 1):
        diff = abs(arr[i+1] - arr[i])
        differences.append(diff)
    return differences
if __name__ == '__main__':
    sample_array_1 = [1, 3, 2, 5, 4]
    result_1 = find_adjacent_differences(sample_array_1)
    print(result_1)
    sample_array_2 = [10, 8, 6, 4, 2]
    result_2 = find_adjacent_differences(sample_array_2)
    print(result_2)
    sample_array_3 = [5, 5, 5, 5]
    result_3 = find_adjacent_differences(sample_array_3)
    print(result_3)
    sample_array_4 = [100, 0, -50, 150]
    result_4 = find_adjacent_differences(sample_array_4)
    print(result_4)
    sample_array_5 = [7]
    result_5 = find_adjacent_differences(sample_array_5)
    print(result_5)