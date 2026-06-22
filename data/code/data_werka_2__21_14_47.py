def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less_than_pivot = []
    equal_to_pivot = []
    greater_than_pivot = []

    for num in arr:
        if num < pivot:
            less_than_pivot.append(num)
        elif num == pivot:
            equal_to_pivot.append(num)
        else:
            greater_than_pivot.append(num)

    return quicksort(less_than_pivot) + equal_to_pivot + quicksort(greater_than_pivot)

if __name__ == '__main__':
    sample_values = [4, 2, 5, 1, 3]
    sorted_values = quicksort(sample_values)
    print(sorted_values)