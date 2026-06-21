MAX_INT = float('-inf')

def max_subarray_sum(arr):
    max_current = max_global = MAX_INT
    for num in arr:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

if __name__ == '__main__':
    sample_values = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(sample_values))