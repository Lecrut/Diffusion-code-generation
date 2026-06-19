def compare_adjacent(arr):
    result = []
    n = len(arr)
    if n < 2:
        return result
    for i in range(n - 1):
        result.append(arr[i] <= arr[i + 1])
    return result

if __name__ == '__main__':
    sample_array = [3, 5, 4, 8, 6, 9, 7]
    result = compare_adjacent(sample_array)
    print(result)