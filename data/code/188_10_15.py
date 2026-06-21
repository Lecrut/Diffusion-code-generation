class ListReverser:
    def reverse_list(self, arr):
        return arr[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", my_list)
    reversed_list = reverser.reverse_list(my_list)
    print("Reversed list:", reversed_list)
    
    my_list_2 = [10, 20, 30, 40, 50]
    print("Original list:", my_list_2)
    reversed_list_2 = reverser.reverse_list(my_list_2)
    print("Reversed list:", reversed_list_2)