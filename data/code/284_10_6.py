class ListReverser:
    def reverse_list(self, input_list):
        return input_list[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    print("Original list:", sample_list)
    reversed_list = reverser.reverse_list(sample_list)
    print("Reversed list:", reversed_list)
    sample_list_2 = ['a', 'b', 'c', 'd']
    print("\nOriginal list:", sample_list_2)
    reversed_list_2 = reverser.reverse_list(sample_list_2)
    print("Reversed list:", reversed_list_2)
    sample_list_3 = [10, 20, 30, 40]
    print("\nOriginal list:", sample_list_3)
    reversed_list_3 = reverser.reverse_list(sample_list_3)
    print("Reversed list:", reversed_list_3)