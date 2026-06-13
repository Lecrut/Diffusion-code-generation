class Store:
    def __init__(self):
        self.items = {}
    def add_item(self, name, quantity):
        if not isinstance(name, str) or not name:
            raise ValueError("Store item name must be a non-empty string.")
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
        print("\nRetrieving item details:")
        apple_quantity = my_store.get_item("Apples")
        print(f"Quantity of Apples: {apple_quantity}")
        try:
            unknown_quantity = my_store.get_item("Grapes")
            print(f"Quantity of Grapes: {unknown_quantity}")
        except KeyError as e:
            print(f"Error caught: {e}")
        print("\nDisplaying store contents:")
        my_store.display_store()
        print("\nTesting error handling:")
        try:
            my_store.add_item("", 50)
        except ValueError as e:
            print(f"Error caught for invalid name: {e}")
        try:
            my_store.add_item("Pears", -10)
        except ValueError as e:
            print(f"Error caught for invalid quantity: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")