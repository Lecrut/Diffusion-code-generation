def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    sample_values = [3.5, 2.1, 4.8, 1.9, 5.6, 2.7, 3.0]
    sorted_values = quicksort(sample_values)
    print(sorted_values)