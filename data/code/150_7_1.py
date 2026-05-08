class EfficientList:
    def __init__(self, initial_list):
        self.data = list(initial_list)
    def remove_by_value(self, value):
        try:
            index_to_remove = self.data.index(value)
            self.data.pop(index_to_remove)
        except ValueError:
            pass
if __name__ == '__main__':
    sample_list = [10, 20, 30, 20, 40, 10]
    efficient_list = EfficientList(sample_list)
    print("Original list:", sample_list)
    efficient_list.remove_by_value(20)
    print("After removing first occurrence of 20:", efficient_list.data)
    efficient_list.remove_by_value(10)
    print("After removing first occurrence of 10:", efficient_list.data)
    efficient_list.remove_by_value(99)
    print("After attempting to remove non-existent value:", efficient_list.data)
    sample_list_2 = [5, 1, 8, 5, 9]
    efficient_list_2 = EfficientList(sample_list_2)
    print("\nOriginal list 2:", sample_list_2)
    efficient_list_2.remove_by_value(5)
    print("After removing first occurrence of 5:", efficient_list_2.data)