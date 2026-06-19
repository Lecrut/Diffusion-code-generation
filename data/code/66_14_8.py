def compare_adjacent_elements(arr):
    return [arr[i] > arr[i - 1] for i in range(1, len(arr))]

if __name__ == '__main__':
    SAMPLE_ARRAY = [3, 5, 2, 8, 6]
    result = compare_adjacent_elements(SAMPLE_ARRAY)
    print(result)