def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickselect_median(arr):
    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr)//2)
    else:
        return 0.5 * (quickselect(arr, len(arr)//2 - 1) + quickselect(arr, len(arr)//2))

def quickselect(arr, k):
    low = 0
    high = len(arr) - 1
    while True:
        pivot_index = partition(arr, low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

if __name__ == '__main__':
    sample_list1 = [3.5, 1.2, 8.9, 4.1, 2.3]
    print(f"Sample List 1: {sample_list1}")
    median1 = quickselect_median(sample_list1)
    print(f"Median 1: {median1}")

    sample_list2 = [10.0, 5.0, 2.0, 7.0, 1.0]
    print(f"Sample List 2: {sample_list2}")
    median2 = quickselect_median(sample_list2)
    print(f"Median 2: {median2}")

    sample_list3 = [1.0, 2.0, 3.0, 4.0]
    print(f"Sample List 3: {sample_list3}")
    median3 = quickselect_median(sample_list3)
    print(f"Median 3: {median3}")

    sample_list4 = [1.5, 2.5, 3.5, 4.5]
    print(f"Sample List 4: {sample_list4}")
    median4 = quickselect_median(sample_list4)
    print(f"Median 4: {median4}")