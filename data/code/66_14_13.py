def is_greater_than_previous(arr):
    return [arr[i] > arr[i - 1] for i in range(1, len(arr))]

if __name__ == '__main__':
    sample_array = [5.0, 3.2, 4.8, 6.5, 6.5, 7.1]
    result = is_greater_than_previous(sample_array)
    print(result)