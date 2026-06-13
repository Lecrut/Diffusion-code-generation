class Store:
    def __init__(self):
        self.items = {}
    def add_item(self, item_name, quantity):
        if not isinstance(item_name, str) or not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Invalid input: Item name must be a string and quantity must be a positive integer.")
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
    def get_item(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            raise KeyError(f"Item '{item_name}' not found in the store.")
    def display_store_details(self):
        print("--- Store Details ---")
        if not self.items:
            print("The store is currently empty.")
            return
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")
        print("---------------------")
if __name__ == '__main__':
    my_store = Store()
    try:
        my_store.add_item("Apples", 10)
        my_store.add_item("Bananas", 5)
        my_store.add_item("Oranges", 12)
        my_store.add_item("Apples", 3)
        my_store.display_store_details()
        print("\nAttempting to retrieve item:")
        try:
            apple_count = my_store.get_item("Apples")
            print(f"Quantity of Apples: {apple_count}")
            invalid_item = my_store.get_item("Grapes")
        except KeyError as e:
            print(e)
        print("\nAttempting to add invalid item (Error Handling Test):")
        try:
            my_store.add_item("Pears", -2)
        except ValueError as e:
            print(f"Caught expected error: {e}")
        try:
            my_store.add_item(123, 5)
        except ValueError as e:
            print(f"Caught expected error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")