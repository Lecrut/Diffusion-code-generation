def compare_adjacent_elements(arr):
    return [b > a for a, b in zip(arr, arr[1:])]

if __name__ == '__main__':
    SAMPLE_ARRAY = [7, 3, 5, 2, 8, 6]
    result = compare_adjacent_elements(SAMPLE_ARRAY)
    print(result)