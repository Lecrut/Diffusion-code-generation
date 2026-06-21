class ListReverser:
    @staticmethod
    def reverse_list(input_list):
        start = 0
        end = len(input_list) - 1
        while start < end:
            input_list[start], input_list[end] = input_list[end], input_list[start]
            start += 1
            end -= 1
        return input_list

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    reversed_list_1 = ListReverser.reverse_list(sample_list_1.copy())
    print(f"Original list: {sample_list_1}")
    print(f"Reversed list: {reversed_list_1}")

    sample_list_2 = ['a', 'b', 'c', 'd']
    reversed_list_2 = ListReverser.reverse_list(sample_list_2.copy())
    print(f"Original list: {sample_list_2}")
    print(f"Reversed list: {reversed_list_2}")

    sample_list_3 = [10, 20, 30]
    reversed_list_3 = ListReverser.reverse_list(sample_list_3.copy())
    print(f"Original list: {sample_list_3}")
    print(f"Reversed list: {reversed_list_3}")