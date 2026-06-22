def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left = []
    right = []
    middle = [pivot]
    
    for i in range(len(arr)):
        if i == pivot_index:
            continue
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            middle.append(arr[i])
    
    return quicksort(left) + middle + quicksort(right)

if __name__ == '__main__':
    sample_values = [9, 3, 7, 5, 6, 4, 8, 2]
    sorted_values = quicksort(sample_values)
    print(sorted_values)