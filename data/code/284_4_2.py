def reverse_list_swaps(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
if __name__ == '__main__':
    data = [5, 1, 4, 2, 8]
    print("Original list:", data)
    reversed_data = reverse_list_swaps(data)
    print("Reversed list:", reversed_data)