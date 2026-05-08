class ListManipulator:
    def get_reversed_list(self, input_list):
        return input_list[::-1]
if __name__ == '__main__':
    manipulator = ListManipulator()
    sample_list_1 = [1, 2, 3, 4, 5]
    reversed_list_1 = manipulator.get_reversed_list(sample_list_1)
    print(f"Original list: {sample_list_1}")
    print(f"Reversed list: {reversed_list_1}")
    sample_list_2 = ['a', 'b', 'c', 'd']
    reversed_list_2 = manipulator.get_reversed_list(sample_list_2)
    print(f"Original list: {sample_list_2}")
    print(f"Reversed list: {reversed_list_2}")
    sample_list_3 = [10, 20, 30]
    reversed_list_3 = manipulator.get_reversed_list(sample_list_3)
    print(f"Original list: {sample_list_3}")
    print(f"Reversed list: {reversed_list_3}")