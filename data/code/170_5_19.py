class Inventory:

    def __init__(self):
        self.items = []

    def add_item(self, item_name, quantity):
        index = bisect.bisect_left(self.items, (item_name, 0))
        if index < len(self.items) and self.items[index][0] == item_name:
            _, q = self.items[index]
            self.items[index] = (item_name, q + quantity)
        else:
            bisect.insort(self.items, (item_name, quantity))

    def lookup_item(self, item_name):
        index = bisect.bisect_left(self.items, (item_name, 0))
        if index < len(self.items) and self.items[index][0] == item_name:
            return self.items[index][1]
        return None
if __name__ == '__main__':
    inventory = Inventory()
    inventory.add_item('Apples', 50)
    inventory.add_item('Bananas', 120)
    inventory.add_item('Oranges', 75)
    inventory.add_item('Grapes', 30)
    inventory.add_item('Pears', 45)
    print(inventory.lookup_item('Apples'))
    print(inventory.lookup_item('Bananas'))
    print(inventory.lookup_item('Oranges'))
    print(inventory.lookup_item('Grapes'))
    print(inventory.lookup_item('Pears'))