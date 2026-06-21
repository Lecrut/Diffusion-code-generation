class ListReverser:
    def reverse_in_place(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    reverser = ListReverser()
    list1 = [1, 2, 3, 4, 5]
    print(f"Original list 1: {list1}")
    reverser.reverse_in_place(list1)
    print(f"Reversed list 1: {list1}")
    
    list2 = [10, 20, 30, 40, 50, 60]
    print(f"Original list 2: {list2}")
    reverser.reverse_in_place(list2)
    print(f"Reversed list 2: {list2}")
    
    list3 = [1, 2, 2, 3, 4]
    print(f"Original list 3: {list3}")
    reverser.reverse_in_place(list3)
    print(f"Reversed list 3: {list3}")