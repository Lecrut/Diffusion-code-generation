from collections import defaultdict

class Inventory:
    ITEM_KEY = "item_id"
    NAME_KEY = "name"
    QUANTITY_KEY = "quantity"

    def __init__(self):
        self.items = defaultdict(dict)

    def add_item(self, item_data: dict):
        if item_data[self.ITEM_KEY] in self.items:
            raise ValueError(f"Item ID {item_data[self.ITEM_KEY]} already exists in the inventory.")
        self.items[item_data[self.ITEM_KEY]] = {
            self.NAME_KEY: item_data.get(self.NAME_KEY, ""),
            self.QUANTITY_KEY: item_data.get(self.QUANTITY_KEY, 0)
        }

    def add_batch_items(self, batch_data: list):
        for item_data in batch_data:
            self.add_item(item_data)

    def calculate_total_value(self, item_prices: dict) -> float:
        total_value = 0.0
        for item_id, quantity in self.items.items():
            if item_id in item_prices:
                total_value += item_prices[item_id] * quantity[self.QUANTITY_KEY]
        return total_value

if __name__ == '__main__':
    my_inventory = Inventory()
    batch_items = [
        {Inventory.ITEM_KEY: 101, Inventory.NAME_KEY: "Apple", Inventory.QUANTITY_KEY: 50},
        {Inventory.ITEM_KEY: 102, Inventory.NAME_KEY: "Banana", Inventory.QUANTITY_KEY: 30}
    ]
    my_inventory.add_batch_items(batch_items)
    item_prices = {101: 0.5, 102: 0.2}
    print(f"Total inventory value: ${my_inventory.calculate_total_value(item_prices):.2f}")