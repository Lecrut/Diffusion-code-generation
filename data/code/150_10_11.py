class ListModifier:
    def __init__(self, initial_list):
        self.items = initial_list

    def remove_item(self, item_to_remove):
        if item_to_remove in self.items:
            self.items = [item for item in self.items if item != item_to_remove]

if __name__ == '__main__':
    modifier = ListModifier([1, 2, 3, 4, 5])
    modifier.remove_item(3)
    print(modifier.items)