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
    initial_list = [10, 20, 30, 20, 40, 20]
    efficient_list = EfficientList(initial_list)
    print(f"Initial list: {initial_list}")
    value_to_remove_1 = 20
    efficient_list.remove_by_value(value_to_remove_1)
    print(f"After removing {value_to_remove_1}: {efficient_list.data}")
    value_to_remove_2 = 40
    efficient_list.remove_by_value(value_to_remove_2)
    print(f"After removing {value_to_remove_2}: {efficient_list.data}")
    value_to_remove_3 = 99
    efficient_list.remove_by_value(value_to_remove_3)
    print(f"After attempting to remove {value_to_remove_3}: {efficient_list.data}")