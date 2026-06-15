class Store:
    def __init__(self):
        self.items = {}
    def add_item(self, name, quantity):
        if not isinstance(name, str) or not name:
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.items[name] = quantity
    def get_item(self, name):
        if name in self.items:
            return self.items[name]
        else:
            raise KeyError(f"Item '{name}' not found in the store.")
    def display_store(self):
        if not self.items:
            print("The store is currently empty.")
            return
        print("--- Store Details ---")
        for item, quantity in self.items.items():
            print(f"Item: {item}, Quantity: {quantity}")
        print("---------------------")
if __name__ == '__main__':
    my_store = Store()
    try:
        my_store.add_item("Apples", 100)
        my_store.add_item("Bananas", 150)
        my_store.add_item("Oranges", 75)
        print("Items added successfully.")
        print("\nAttempting to retrieve item 'Apples':")
        apple_quantity = my_store.get_item("Apples")
        print(f"Quantity of Apples: {apple_quantity}")
        print("\nAttempting to retrieve item 'Grapes':")
        grape_quantity = my_store.get_item("Grapes")
    except ValueError as e:
        print(f"\nError during addition: {e}")
    except KeyError as e:
        print(f"\nError during retrieval: {e}")
    finally:
        my_store.display_store()
    print("\nTesting invalid input handling:")
    try:
        my_store.add_item("", 50)
    except ValueError as e:
        print(f"Caught expected error for empty name: {e}")
    try:
        my_store.add_item("Pears", -10)
    except ValueError as e:
        print(f"Caught expected error for negative quantity: {e}")
    try:
        my_store.get_item("Watermelons")
    except KeyError as e:
        print(f"Caught expected error for missing item: {e}")