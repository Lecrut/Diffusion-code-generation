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
        print("--- Store Details ---")
        for item, quantity in self.items.items():
            print(f"Item: {item}, Quantity: {quantity}")
        print("---------------------")
if __name__ == '__main__':
    my_store = Store()
    try:
        my_store.add_item("Apples", 50)
        my_store.add_item("Bananas", 120)
        my_store.add_item("Oranges", 75)
        print("Attempting to retrieve item 'Apples':")
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
        print("\nDisplaying store contents:")
        my_store.display_store()
        print("\nAttempting to add invalid item (negative quantity):")
        try:
            my_store.add_item("Grapes", -10)
        except ValueError as e:
            print(f"Error caught: {e}")
        print("\nAttempting to add invalid item (non-integer quantity):")
        try:
            my_store.add_item("Pears", "twenty")
        except ValueError as e:
            print(f"Error caught: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")