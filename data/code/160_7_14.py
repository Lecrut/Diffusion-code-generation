class UniqueItemList:
    def __init__(self):
        self._item_names = []

    def add_items(self, names):
        for name in names:
            if name not in self._item_names:
                self._item_names.append(name)

    def get_all_names(self):
        return self._item_names

if __name__ == '__main__':
    list_manager = UniqueItemList()
    sample_names_1 = ["Apple", "Banana", "Cherry"]
    sample_names_2 = ["Date", "Elderberry"]
    list_manager.add_items(sample_names_1)
    list_manager.add_items(sample_names_2)
    print(list_manager.get_all_names())