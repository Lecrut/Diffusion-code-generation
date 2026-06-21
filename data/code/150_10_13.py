class ListModifier:
    def __init__(self, items):
        self.items = items

    def remove_item(self, item_to_remove):
        if item_to_remove in self.items:
            self.items = [item for item in self.items if item != item_to_remove]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    modifier = ListModifier(sample_list)
    modifier.remove_item(3)
    print(modifier.items)