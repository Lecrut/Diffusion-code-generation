class ListReverser:
    def reverse_list(self, data):
        left = 0
        right = len(data) - 1
        while left < right:
            temp = data[left]
            data[left] = data[right]
            data[right] = temp
            left += 1
            right -= 1
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    reverser = ListReverser()
    print("Original list:", my_list)
    reverser.reverse_list(my_list)
    print("Reversed list:", my_list)
    my_list_2 = ['a', 'b', 'c', 'd', 'e']
    reverser_2 = ListReverser()
    print("Original list:", my_list_2)
    reverser_2.reverse_list(my_list_2)
    print("Reversed list:", my_list_2)