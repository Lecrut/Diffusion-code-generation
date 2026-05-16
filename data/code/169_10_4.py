def manage_item_counts():
    item_counts = {}
    def add_item(item, count):
        if not isinstance(item, str) or not isinstance(count, int) or count < 0:
            raise ValueError("Invalid input: item must be a string and count must be a non-negative integer.")
        if item in item_counts:
            item_counts[item] += count
        else:
            item_counts[item] = count
    def get_count(item):
        if item in item_counts:
            return item_counts[item]
        else:
            raise KeyError(f"Item '{item}' not found in counts.")
    def update_count(item, change):
        if item not in item_counts:
            raise KeyError(f"Cannot update: Item '{item}' not found.")
        new_count = item_counts[item] + change
        if new_count < 0:
            raise ValueError(f"Update resulted in negative count for {item}.")
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
        print("\nAfter additions:")
        display()
        print("\nRetrieving counts:")
        print(f"Apples count: {get('apples')}")
        try:
            print(f"oranges count: {get('oranges')}")
        except KeyError as e:
            print(e)
        print("\nUpdating counts:")
        update("bananas", -2)
        update("grapes", 20)
        print("\nFinal state:")
        display()
        try:
            get("nonexistent")
        except KeyError as e:
            print(f"Error caught: {e}")
        try:
            update("apples", -100)
        except ValueError as e:
            print(f"Error caught: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")