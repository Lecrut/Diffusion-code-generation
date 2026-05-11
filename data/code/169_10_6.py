def manage_item_counts():
    item_counts = {}
    def add_item(item, count):
        if not isinstance(item, str) or not isinstance(count, int) or count < 0:
            raise ValueError("Invalid item or count provided.")
        item_counts[item] = item_counts.get(item, 0) + count
    def get_count(item):
        if item in item_counts:
            return item_counts[item]
        return 0
    def update_count(item, new_count):
        if not isinstance(new_count, int) or new_count < 0:
            raise ValueError("Invalid new count provided.")
        if item not in item_counts:
            raise KeyError(f"Item '{item}' not found.")
        item_counts[item] = new_count
    def display_counts():
        print("--- Item Counts ---")
        if not item_counts:
            print("No items currently tracked.")
            return
        for item, count in sorted(item_counts.items()):
            print(f"{item}: {count}")
        print("-------------------")
    return item_counts, add_item, get_count, update_count, display_counts
if __name__ == '__main__':
    counts, add, get, update, display = manage_item_counts()
    print("Initial state:")
    display()
    try:
        add("apples", 10)
        add("bananas", 5)
        add("apples", 3)
        add("oranges", 12)
        print("\nAfter additions:")
        display()
        print("\nRetrieving counts:")
        print(f"Apples: {get('apples')}")
        print(f"Bananas: {get('bananas')}")
        print(f"Grapes (non-existent): {get('grapes')}")
        print("\nUpdating counts:")
        update("apples", 15)
        update("bananas", 8)
        print("\nFinal state after updates:")
        display()
        try:
            update("grapes", 5)
        except KeyError as e:
            print(f"Error caught: {e}")
        try:
            update("apples", -1)
        except ValueError as e:
            print(f"Error caught: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")