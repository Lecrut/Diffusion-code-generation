class ListReverser:
    def __init__(self, data_list):
        self.data_list = data_list

    def reverse_in_place(self):
        self.data_list.reverse()

if __name__ == '__main__':
    my_list_reverser = ListReverser([1, 2, 3, 4, 5])
    print("Original list:", my_list_reverser.data_list)
    my_list_reverser.reverse_in_place()
    print("Reversed list:", my_list_reverser.data_list)

    another_list_reverser = ListReverser(['a', 'b', 'c', 'd'])
    print("Original list:", another_list_reverser.data_list)
    another_list_reverser.reverse_in_place()
    print("Reversed list:", another_list_reverser.data_list)