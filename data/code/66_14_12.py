def compare_adjacent_elements(arr):
    return [arr[i] > arr[i - 1] for i in range(1, len(arr))]

if __name__ == '__main__':
    SAMPLE_ARRAY = [10, 20, 20, 30, 25, 40]
    result = compare_adjacent_elements(SAMPLE_ARRAY)
    print(result)