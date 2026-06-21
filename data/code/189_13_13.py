class ListModifier:
    def __init__(self, initial_list):
        self.data = initial_list

    def remove_value(self, value_to_remove):
        self.data = [x for x in self.data if x != value_to_remove]
        return self.data

if __name__ == '__main__':
    modifier = ListModifier([1, 2, 3, 4, 2, 5])
    item_to_remove = 2
    modified_list = modifier.remove_value(item_to_remove)
    print(f"Original list: [1, 2, 3, 4, 2, 5]")
    print(f"Item to remove: {item_to_remove}")
    print(f"Modified list: {modified_list}")