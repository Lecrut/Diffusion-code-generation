class ListManager:
    def __init__(self, items):
        self.items = items

    def remove_item(self, item):
        for i, lst in enumerate(self.items):
            try:
                lst.remove(item)
                break
            except ValueError:
                continue

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    manager = ListManager([sample_list])
    item_to_remove = 3
    manager.remove_item(item_to_remove)
    print(manager.items[0])