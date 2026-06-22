def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    right = []
    middle = []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    sample_values = [9, 7, 5, 11, 2, 4, 6]
    sorted_values = quicksort(sample_values)
    print(sorted_values)