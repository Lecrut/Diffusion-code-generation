class ItemContainer:
    def __init__(self):
        self._item_names = []
    def add_item_names(self, names):
        self._item_names.extend(names)
    def get_all_names(self):
        return self._item_names
if __name__ == '__main__':
    container = ItemContainer()
    sample_names_1 = ["Apple", "Banana", "Cherry"]
    sample_names_2 = ["Date", "Elderberry"]
    container.add_item_names(sample_names_1)
    container.add_item_names(sample_names_2)
    all_names = container.get_all_names()
    print(all_names)