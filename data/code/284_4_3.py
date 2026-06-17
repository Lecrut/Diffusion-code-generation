def reverse_list_swaps(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
if __name__ == '__main__':
    my_list = [5, 1, 4, 2, 8]
    print("Original list:", my_list)
    reversed_list = reverse_list_swaps(my_list)
    print("Reversed list:", reversed_list)
    my_list_2 = [10, 5, 2, 7, 1]
    print("Original list:", my_list_2)
    reversed_list_2 = reverse_list_swaps(my_list_2)
    print("Reversed list:", reversed_list_2)
    my_list_3 = [1, 2, 3, 4, 5]
    print("Original list:", my_list_3)
    reversed_list_3 = reverse_list_swaps(my_list_3)
    print("Reversed list:", reversed_list_3)