class ItemStore:
    def __init__(self):
        self._items = []
    def add_items(self, names):
        self._items.extend(names)
    def get_all_names(self):
        return self._items
if __name__ == '__main__':
    store = ItemStore()
    sample_names_1 = ["Apple", "Banana", "Cherry"]
    sample_names_2 = ["Date", "Elderberry"]
    store.add_items(sample_names_1)
    store.add_items(sample_names_2)
    retrieved_names = store.get_all_names()
    print(retrieved_names)