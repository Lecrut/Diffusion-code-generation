class ListManipulator:
    def concatenate_lists(self, list1, list2):
        return list1 + list2
if __name__ == '__main__':
    manipulator = ListManipulator()
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result = manipulator.concatenate_lists(list_a, list_b)
    print(result)