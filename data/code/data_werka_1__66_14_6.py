def compare_adjacent_elements(arr):
    return [b > a for a, b in zip(arr, arr[1:])]

if __name__ == '__main__':
    sample_array = [1.0, 2.5, 3.0, 3.0, 5.1, 6.0, 6.0, 7.5]
    result = compare_adjacent_elements(sample_array)
    print(result)