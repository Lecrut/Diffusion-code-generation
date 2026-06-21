class ListModifier:
    def __init__(self, initial_list):
        self.list = initial_list

    def remove_item(self, item_to_remove):
        self.list = [x for x in self.list if x != item_to_remove]

if __name__ == '__main__':
    modifier = ListModifier([1, 2, 3, 4, 2, 5])
    print(f"Original list: {modifier.list}")
    modifier.remove_item(2)
    print(f"Item removed: 2")
    print(f"New list: {modifier.list}")