class ListReverser:
    @staticmethod
    def reverse_recursive(data):
        if len(data) <= 1:
            return data
        else:
            return [data[-1]] + ListReverser.reverse_recursive(data[:-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original list:", sample_list)
    reversed_list = ListReverser.reverse_recursive(sample_list)
    print("Reversed list:", reversed_list)

    another_list = ['a', 'b', 'c', 'd']
    print("Original list:", another_list)
    reversed_another_list = ListReverser.reverse_recursive(another_list)
    print("Reversed list:", reversed_another_list)

    empty_list = []
    print("Original list:", empty_list)
    reversed_empty_list = ListReverser.reverse_recursive(empty_list)
    print("Reversed list:", reversed_empty_list)

    single_element_list = [7]
    print("Original list:", single_element_list)
    reversed_single_element_list = ListReverser.reverse_recursive(single_element_list)
    print("Reversed list:", reversed_single_element_list)