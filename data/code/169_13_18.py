class ItemInventory:

    def __init__(self):
        self.items = []

    def insert_item(self, item_id, count):
        if not self.items or self.items[-1][0] != item_id:
            self.items.append((item_id, count))
        else:
            self.items[-1] = (item_id, self.items[-1][1] + count)

    def update_item(self, item_id, count):
        for i in range(len(self.items)):
            if self.items[i][0] == item_id:
                self.items[i] = (item_id, self.items[i][1] + count)
                return
        raise KeyError(f'Item {item_id} not found')

    def delete_item(self, item_id):
        for i in range(len(self.items)):
            if self.items[i][0] == item_id:
                del self.items[i]
                return
        raise KeyError(f'Item {item_id} not found')
if __name__ == '__main__':
    inventory = ItemInventory()
    inventory.insert_item(1, 5)
    inventory.insert_item(2, 3)
    inventory.update_item(1, 2)
    inventory.delete_item(2)
    print(inventory.items)