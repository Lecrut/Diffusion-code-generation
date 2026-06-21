class ItemInventory:
    def __init__(self):
        self.items = []

    def insert_item(self, item_id, count):
        for i, (id, _) in enumerate(self.items):
            if id == item_id:
                self.items[i] = (item_id, count)
                return
        self.items.append((item_id, count))

    def update_item_count(self, item_id, count):
        for i, (id, _) in enumerate(self.items):
            if id == item_id:
                self.items[i] = (item_id, count)
                return

    def delete_item(self, item_id):
        for i, (id, _) in enumerate(self.items):
            if id == item_id:
                del self.items[i]
                break

if __name__ == '__main__':
    inventory = ItemInventory()
    inventory.insert_item(101, 5)
    inventory.update_item_count(101, 10)
    inventory.delete_item(101)