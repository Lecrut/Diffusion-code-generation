def reverse_list_inplace(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", my_list)
    reverse_list_inplace(my_list)
    print("Reversed list:", my_list)
    my_list_2 = [10, 20, 30, 40, 50]
    print("Original list:", my_list_2)
    reverse_list_inplace(my_list_2)
    print("Reversed list:", my_list_2)
    my_list_3 = [1, 2, 2, 3, 1]
    print("Original list:", my_list_3)
    reverse_list_inplace(my_list_3)
    print("Reversed list:", my_list_3)