def reverse_in_place(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print("Original list 1:", list1)
    reverse_in_place(list1)
    print("Reversed list 1:", list1)
    list2 = [10, 20, 30, 40, 50, 60]
    print("Original list 2:", list2)
    reverse_in_place(list2)
    print("Reversed list 2:", list2)
    list3 = [1, 2, 2, 3, 4]
    print("Original list 3:", list3)
    reverse_in_place(list3)
    print("Reversed list 3:", list3)
    list4 = [5]
    print("Original list 4:", list4)
    reverse_in_place(list4)
    print("Reversed list 4:", list4)
    list5 = []
    print("Original list 5:", list5)
    reverse_in_place(list5)
    print("Reversed list 5:", list5)