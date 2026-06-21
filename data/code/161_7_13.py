class ItemStore:
    def __init__(self):
        self.items = {}

    def initialize_items(self):
        self.items['apple'] = 100
        self.items['banana'] = 150
        self.items['cherry'] = 200

    def get_item_price(self, item_name):
        return self.items.get(item_name)

if __name__ == '__main__':
    store = ItemStore()
    store.initialize_items()
    print(f"Price of apple: {store.get_item_price('apple')}")
    print(f"Price of banana: {store.get_item_price('banana')}")
    print(f"Price of grape: {store.get_item_price('grape')}")