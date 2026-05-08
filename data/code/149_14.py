class ListManipulator:
    def get_reversed_list(self, input_list):
        return input_list[::-1]
if __name__ == '__main__':
    manipulator = ListManipulator()
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = manipulator.get_reversed_list(sample_list)
    print(reversed_list)