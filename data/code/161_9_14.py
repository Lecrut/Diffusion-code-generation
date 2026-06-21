class ItemSorter:
    def __init__(self):
        self.items = {
            'apple': 3,
            'banana': 2,
            'cherry': 5,
            'date': 4
        }

    def get_sorted_item_names(self):
        return sorted(self.items.keys())

if __name__ == '__main__':
    sorter = ItemSorter()
    sorted_items = sorter.get_sorted_item_names()
    print(sorted_items)