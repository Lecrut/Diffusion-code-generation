class ListManipulator:
    def __init__(self, initial_list):
        self.list = initial_list

    @staticmethod
    def is_valid_index(lst, index):
        return 0 <= index < len(lst)

    def pop_element(self, index):
        if not self.is_valid_index(self.list, index):
            print("Error: Index is out of bounds.")
            return None
        return self.list.pop(index)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    manipulator = ListManipulator(sample_list)
    index_to_pop = 2
    popped_element = manipulator.pop_element(index_to_pop)
    print("Popped element:", popped_element)
    print("Remaining list:", sample_list)