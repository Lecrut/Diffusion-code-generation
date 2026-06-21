class InventoryManager:
    def __init__(self):
        self.items = []

    def insert_item(self, item_name, count):
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                self.items[i][1] += count
                return
        self.items.append([item_name, count])

    def update_item(self, item_name, count):
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                self.items[i][1] = count
                return

    def delete_item(self, item_name):
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                del self.items[i]
                return

if __name__ == '__main__':
    inventory = InventoryManager()
    inventory.insert_item('apple', 10)
    inventory.update_item('banana', 5)
    inventory.delete_item('apple')
    print(inventory.items)