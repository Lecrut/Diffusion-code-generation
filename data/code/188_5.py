class ListUtility:
    @staticmethod
    def reverse_list(data):
        data.reverse()
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)
    ListUtility.reverse_list(my_list)
    print("Reversed list:", my_list)
    another_list = ['a', 'b', 'c', 'd']
    print("Original list:", another_list)
    ListUtility.reverse_list(another_list)
    print("Reversed list:", another_list)