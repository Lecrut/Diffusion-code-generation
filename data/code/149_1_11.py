def reverse_in_place(arr):
    arr.reverse()

if __name__ == '__main__':
    list1 = [5, 4, 3, 2, 1]
    print(f"Original list 1: {list1}")
    reverse_in_place(list1)
    print(f"Reversed list 1: {list1}")

    list2 = [60, 50, 40, 30, 20, 10]
    print(f"Original list 2: {list2}")
    reverse_in_place(list2)
    print(f"Reversed list 2: {list2}")

    list3 = [4, 3, 2, 2, 1]
    print(f"Original list 3: {list3}")
    reverse_in_place(list3)
    print(f"Reversed list 3: {list3}")