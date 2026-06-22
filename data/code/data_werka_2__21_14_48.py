def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    sample_values = [9, 3, 7, 6, 2, 8, 5, 1]
    sorted_values = quicksort(sample_values)
    print(sorted_values)