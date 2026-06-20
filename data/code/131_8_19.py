MAX_SUBARRAY_SUM = float('-inf')

def max_subarray_sum(arr):
    current_max = global_max = MAX_SUBARRAY_SUM
    for num in arr:
        current_max = max(num, current_max + num)
        if current_max > global_max:
            global_max = current_max
    return global_max

if __name__ == '__main__':
    sample_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_subarray_sum(sample_array))