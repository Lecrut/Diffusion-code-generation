def manage_item_counts(data):
    def add_item(item, count):
        if item in data:
            data[item] += count
        else:
            data[item] = count
    def get_count(item):
        if item in data:
            return data[item]
        else:
            return 0
    def update_count(item, new_count):
        if item in data:
            if new_count >= 0:
                data[item] = new_count
            else:
                raise ValueError("Count cannot be negative")
        else:
            data[item] = new_count
    def display_counts(data):
        print("--- Item Counts ---")
        if not data:
            print("No items found.")
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
    item_data = {"apple": 10, "banana": 5, "orange": 12}
    operations = manage_item_counts(item_data)
    print("Initial Data:", item_data)
    operations["add"]("apple", 7)
    operations["add"]("grape", 20)
    operations["add"]("banana", 3)
    print("After Add Operations:", item_data)
    print("Count of apple:", operations["get"]("apple"))
    print("Count of kiwi (new item):", operations["get"]("kiwi"))
    operations["update"]("orange", 15)
    print("After Update Operation:", item_data)
    try:
        operations["update"]("apple", -5)
    except ValueError as e:
        print(f"Error caught: {e}")
    operations["display"](item_data)