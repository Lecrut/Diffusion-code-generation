class ListReverser:
    def reverse_list(self, input_list):
        reversed_list = []
        start_index = 0
        end_index = len(input_list) - 1
        while start_index <= end_index:
            reversed_list.append(input_list[end_index])
            end_index -= 1
        return reversed_list

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list_1 = [1, 2, 3, 4, 5]
    reversed_list_1 = reverser.reverse_list(sample_list_1)
    print(f"Original list: {sample_list_1}")
    print(f"Reversed list: {reversed_list_1}")

    sample_list_2 = ['a', 'b', 'c', 'd']
    reversed_list_2 = reverser.reverse_list(sample_list_2)
    print(f"Original list: {sample_list_2}")
    print(f"Reversed list: {reversed_list_2}")

    sample_list_3 = [10, 20, 30]
    reversed_list_3 = reverser.reverse_list(sample_list_3)
    print(f"Original list: {sample_list_3}")
    print(f"Reversed list: {reversed_list_3}")