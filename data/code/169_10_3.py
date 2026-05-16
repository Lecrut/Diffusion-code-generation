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
    return add_item, get_count, update_count, display_counts
if __name__ == '__main__':
    initial_data = {
        "apples": 10,
        "bananas": 5,
        "oranges": 15
    }
    add, get, update, display = manage_item_counts(initial_data.copy())
    print("Initial State:")
    display()
    try:
        add("apples", 7)
        add("bananas", 12)
        add("grapes", 20)
        add("apples", -5)                                             
    except ValueError as e:
        print(f"Error during addition: {e}")
    print("\nState after additions:")
    display()
    try:
        count_apples = get("apples")
        print(f"Count of apples: {count_apples}")
        count_kiwi = get("kiwi")
    except KeyError as e:
        print(f"Error retrieving count: {e}")
    try:
        update("oranges", 30)
        print("\nState after update:")
        display()
        update("pears", 5)                                                     
    except KeyError as e:
        print(f"Error during update: {e}")
    try:
        update("bananas", -10)                                          
    except ValueError as e:
        print(f"Error during update: {e}")
    print("\nFinal State:")
    display()