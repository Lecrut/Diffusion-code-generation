def compare_adjacent_elements(arr):
    comparisons = []
    for i in range(1, len(arr)):
        comparisons.append(arr[i] > arr[i - 1])
    return comparisons

if __name__ == '__main__':
    sample_array = [7, 3, 9, 2, 5]
    result = compare_adjacent_elements(sample_array)
    print(result)