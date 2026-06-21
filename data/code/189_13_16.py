class ListModifier:
    def __init__(self, initial_list):
        self.list = initial_list

    def remove_value(self, value_to_remove):
        self.list = [x for x in self.list if x != value_to_remove]
        return self.list

if __name__ == '__main__':
    modifier = ListModifier([1, 2, 3, 4, 2, 5])
    item = 2
    modified_list = modifier.remove_value(item)
    print(f"Original list: [1, 2, 3, 4, 2, 5]")
    print(f"Item to remove: {item}")
    print(f"Modified list: {modified_list}")