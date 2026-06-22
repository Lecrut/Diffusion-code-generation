class ListManipulator:
    def __init__(self, initial_list):
        self.list = initial_list

    def remove_element(self, index):
        try:
            return self.list.pop(index)
        except IndexError:
            raise ValueError("Index out of range")

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    INDEX_TO_POP_1 = 2
    INDEX_TO_POP_2 = 5

    manipulator = ListManipulator(SAMPLE_LIST)

    try:
        popped_element_1 = manipulator.remove_element(INDEX_TO_POP_1)
        print("Popped element 1:", popped_element_1)
        print("List after popping 1:", manipulator.list)
    except ValueError as e:
        print(e)

    try:
        popped_element_2 = manipulator.remove_element(INDEX_TO_POP_2)
        print("Popped element 2:", popped_element_2)
        print("List after popping 2:", manipulator.list)
    except ValueError as e:
        print(e)