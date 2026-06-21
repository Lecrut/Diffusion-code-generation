items = [
    {"id": 1, "name": "Apple", "price": 0.99},
    {"id": 2, "name": "Banana", "price": 0.59},
    {"id": 3, "name": "Cherry", "price": 2.99}
]

class Inventory:
    @staticmethod
    def get_items():
        return items

if __name__ == '__main__':
    inventory = Inventory()
    print(inventory.get_items())