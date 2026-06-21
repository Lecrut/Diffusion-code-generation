class ItemSorter:
    ITEMS = {
        'apple': 3,
        'banana': 2,
        'cherry': 5,
        'date': 4
    }

    @staticmethod
    def get_sorted_item_names():
        return sorted(ItemSorter.ITEMS.keys())

if __name__ == '__main__':
    sorter = ItemSorter()
    print(sorter.get_sorted_item_names())