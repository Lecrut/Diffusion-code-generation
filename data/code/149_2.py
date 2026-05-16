class ListManipulator:
    def reverse_items(self, data_list):
        return data_list[::-1]
if __name__ == '__main__':
    manipulator = ListManipulator()
    sample_list = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_list}")
    reversed_list = manipulator.reverse_items(sample_list)
    print(f"Reversed list: {reversed_list}")