def reverse_list_inplace(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", data)
    reverse_list_inplace(data)
    print("Reversed list:", data)
    data2 = [10, 20, 30, 40, 50]
    print("Original list:", data2)
    reverse_list_inplace(data2)
    print("Reversed list:", data2)
    data3 = [1, 2, 1, 3, 2, 1]
    print("Original list:", data3)
    reverse_list_inplace(data3)
    print("Reversed list:", data3)