MAX_SUBARRAY_SUM = 'max_subarray_sum'

def kadane_algorithm(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global
if __name__ == '__main__':
    sample_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = kadane_algorithm(sample_array)
    print(result)