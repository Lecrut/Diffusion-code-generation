def manage_item_counts(data):
    def add_item(item, count):
        if not isinstance(item, str) or not isinstance(count, int) or count < 0:
            raise ValueError("Invalid item or count provided for addition.")
        data[item] = data.get(item, 0) + count
    def get_count(item):
        if item in data:
            return data[item]
        raise KeyError(f"Item '{item}' not found.")
    def update_count(item, new_count):
        if item not in data:
            raise KeyError(f"Item '{item}' not found for update.")
        if not isinstance(new_count, int) or new_count < 0:
            raise ValueError("New count must be a non-negative integer.")
        data[item] = new_count
    def display_counts():
        print("--- Item Counts ---")
        if not data:
            print("No items currently stored.")
            return
        for item, count in sorted(data.items()):
            print(f"{item}: {count}")
        print("-------------------")
    return {
        "add": add_item,
        "get": get_count,
        "update": update_count,
        "display": display_counts
    }
if __name__ == '__main__':
    initial_data = {
        "apples": 10,
        "bananas": 25
    }
    manager = manage_item_counts(initial_data)
    print("Initial Data:", initial_data)
    try:
        manager["add"]("apples", 5)
        manager["add"]("oranges", 15)
        manager["add"]("bananas", 10)
        print("\nAfter Add Operations:")
        print("Apples count:", manager["get"]("apples"))
        print("Oranges count:", manager["get"]("oranges"))
        print("Bananas count:", manager["get"]("bananas"))
        manager["update"]("apples", 50)
        print("\nAfter Update Operation:")
        print("Apples count:", manager["get"]("apples"))
        manager["update"]("grapes", 5)
        manager["display"]()
        print("\nAttempting to retrieve non-existent item:")
        try:
            manager["get"]("pears")
        except KeyError as e:
            print(f"Caught expected error: {e}")
        print("\nAttempting to update non-existent item:")
        try:
            manager["update"]("kiwis", 10)
        except KeyError as e:
            print(f"Caught expected error: {e}")
        print("\nFinal Data State:")
        print(initial_data)
    except ValueError as e:
        print(f"\nOperation Error: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")