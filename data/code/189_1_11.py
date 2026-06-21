class ListModifier:
    def __init__(self, data):
        self.data = data

    def remove_element(self, value):
        self.data = [item for item in self.data if item != value]

if __name__ == '__main__':
    my_list = [1, 2, 3, 2, 4, 2, 5]
    modifier = ListModifier(my_list)
    value_to_remove = 2
    print("Original list:", modifier.data)
    modifier.remove_element(value_to_remove)
    print("List after removing", value_to_remove, ":", modifier.data)

    my_list_2 = [10, 20, 30, 20, 40, 20]
    modifier = ListModifier(my_list_2)
    value_to_remove_2 = 20
    print("Original list:", modifier.data)
    modifier.remove_element(value_to_remove_2)
    print("List after removing", value_to_remove_2, ":", modifier.data)