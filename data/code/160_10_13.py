class ItemStore:
    MAX_ITEM_LENGTH = 100

    def __init__(self):
        self.items = []

    @staticmethod
    def is_valid_item_name(item_name: str) -> bool:
        return isinstance(item_name, str) and len(item_name.strip()) > 0 and len(item_name.strip()) <= ItemStore.MAX_ITEM_LENGTH

    def add_item(self, item_name: str):
        if self.is_valid_item_name(item_name):
            self.items.append(item_name)

    def get_items(self) -> list:
        return self.items.copy()

if __name__ == '__main__':
    store = ItemStore()
    store.add_item("apple")
    store.add_item("banana")
    print(store.get_items())