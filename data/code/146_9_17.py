def kadane_algorithm(arr):
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

if __name__ == '__main__':
    sample_values = [-2, 3, -4, 5, -3, 2]
    print(kadane_algorithm(sample_values))