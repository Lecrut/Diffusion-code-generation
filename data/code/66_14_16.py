def is_increasing_sequence(arr):
    result = []
    for i in range(1, len(arr)):
        is_greater = arr[i] > arr[i - 1]
        result.append(is_greater)
    return result

if __name__ == '__main__':
    sample_data = [10, 20, 30, 25, 40, 50, 60]
    increasing_status = is_increasing_sequence(sample_data)
    print(increasing_status)