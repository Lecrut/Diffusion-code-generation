class ListModifier:
    def __init__(self, data):
        self.data = data

    def remove_value(self, value):
        self.data = [item for item in self.data if item != value]

if __name__ == '__main__':
    modifier1 = ListModifier([1, 2, 3, 2, 4, 2, 5])
    value_to_remove = 2
    print("Original list:", modifier1.data)
    modifier1.remove_value(value_to_remove)
    print("List after removing", value_to_remove, ":", modifier1.data)

    modifier2 = ListModifier([10, 20, 30, 20, 40, 20])
    value_to_remove_2 = 20
    print("Original list:", modifier2.data)
    modifier2.remove_value(value_to_remove_2)
    print("List after removing", value_to_remove_2, ":", modifier2.data)