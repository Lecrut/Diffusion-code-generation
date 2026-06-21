class InventoryManager:

    def __init__(self):
        self.items = []

    def insert_item(self, item_id, count):
        for i in range(len(self.items)):
            if self.items[i][0] == item_id:
                self.items[i][1] += count
                return
        self.items.append([item_id, count])

    def update_item(self, item_id, count):
        for i in range(len(self.items)):
            if self.items[i][0] == item_id:
                self.items[i][1] = count
                return

    def delete_item(self, item_id):
        for i in range(len(self.items)):
            if self.items[i][0] == item_id:
                del self.items[i]
                return
if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.insert_item('apple', 10)
    inventory.insert_item('banana', 5)
    print(inventory.items)
    inventory.update_item('apple', 20)
    print(inventory.items)
    inventory.delete_item('banana')
    print(inventory.items)