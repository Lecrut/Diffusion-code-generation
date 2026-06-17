def find_adjacent_differences(arr):
    if len(arr) < 2:
        return []
    differences = []
    for i in range(len(arr) - 1):
        diff = abs(arr[i+1] - arr[i])
        differences.append(diff)
    return differences
if __name__ == '__main__':
    sample_array = [1, 5, 3, 8, 2]
    result = find_adjacent_differences(sample_array)
    print(result)