class Store:
    def __init__(self):
        self.items = {}
    def add_item(self, name, quantity):
        if not isinstance(name, str) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid input: Name must be a string and Quantity must be a positive integer.")
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
        print("\n--- Store Details ---")
        for item, quantity in self.items.items():
            print(f"Item: {item}, Quantity: {quantity}")
        print("--------------------")
if __name__ == '__main__':
    my_store = Store()
    try:
        my_store.add_item("Apples", 100)
        my_store.add_item("Bananas", 150)
        my_store.add_item("Oranges", 75)
        print("Items added successfully.")
        print("\nAttempting to retrieve item 'Apples':")
        try:
            quantity = my_store.get_item("Apples")
            print(f"Quantity of Apples: {quantity}")
        except KeyError as e:
            print(e)
        print("\nAttempting to retrieve non-existent item 'Grapes':")
        try:
            my_store.get_item("Grapes")
        except KeyError as e:
            print(e)
        my_store.display_store()
        print("\nTesting error handling for invalid input:")
        try:
            my_store.add_item("Pears", -10)
        except ValueError as e:
            print(f"Caught expected error: {e}")
        try:
            my_store.add_item(123, 50)
        except ValueError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")