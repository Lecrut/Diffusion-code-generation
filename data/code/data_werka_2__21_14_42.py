def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = []
    equal = []
    greater = []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quicksort(less) + equal + quicksort(greater)

if __name__ == '__main__':
    sample_values = [34, 7, 23, 32, 5, 62]
    sorted_values = quicksort(sample_values)
    print(sorted_values)