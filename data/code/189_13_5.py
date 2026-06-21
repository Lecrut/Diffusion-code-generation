class ListModifier:
    def __init__(self, original_list):
        self.original_list = original_list

    def remove_item(self, item_to_remove):
        return [x for x in self.original_list if x != item_to_remove]

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 2, 5]
    modifier = ListModifier(my_list)
    item = 2
    new_list = modifier.remove_item(item)
    print(f"Original list: {my_list}")
    print(f"Item to remove: {item}")
    print(f"New list: {new_list}")