def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []
    
    for x in arr:
        if x < pivot:
            less_than_pivot.append(x)
        elif x > pivot:
            greater_than_pivot.append(x)
        else:
            equal_to_pivot.append(x)
    
    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

if __name__ == '__main__':
    sample_values = [10, 7, 8, 9, 1, 5]
    sorted_values = quicksort(sample_values)
    print(sorted_values)