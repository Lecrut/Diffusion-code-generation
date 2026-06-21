class ListReverser:
    @staticmethod
    def reverse_list(arr):
        return arr[::-1]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7]
    print("Original list:", my_list)
    reversed_list = ListReverser.reverse_list(my_list)
    print("Reversed list:", reversed_list)

    my_list_2 = [10, 20, 30, 40, 50]
    print("Original list:", my_list_2)
    reversed_list_2 = ListReverser.reverse_list(my_list_2)
    print("Reversed list:", reversed_list_2)