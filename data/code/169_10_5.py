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
    item_data = {
        "apples": 10,
        "bananas": 25,
        "oranges": 15
    }
    manager = manage_item_counts(item_data)
    print("Initial Data:", item_data)
    manager["add"]("apples", 5)
    manager["add"]("bananas", 10)
    manager["add"]("grapes", 30)
    print("After Adding:", item_data)
    print("Count of bananas:", manager["get"]("bananas"))
    print("Count of pears (new item):", manager["get"]("pears"))
    manager["update"]("apples", 12)
    print("After Updating apples:", item_data)
    try:
        manager["update"]("oranges", -5)
    except ValueError as e:
        print(f"Error caught: {e}")
    manager["display"](item_data)