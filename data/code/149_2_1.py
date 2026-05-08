class ListManipulator:
    def reverse_items(self, data_list):
        data_list.reverse()
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    manipulator = ListManipulator()
    manipulator.reverse_items(my_list)
    print("Reversed list:", my_list)
    another_list = ['a', 'b', 'c', 'd']
    print("Original list:", another_list)
    manipulator.reverse_items(another_list)
    print("Reversed list:", another_list)