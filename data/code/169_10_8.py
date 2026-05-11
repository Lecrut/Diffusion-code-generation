def manage_item_counts():
    item_counts = {
        "apple": 10,
        "banana": 25,
        "orange": 15
    }
    def add_item(item, quantity):
        if not isinstance(item, str) or not isinstance(quantity, int) or quantity < 0:
            return False
        item_counts[item] = item_counts.get(item, 0) + quantity
        return True
    def get_count(item):
        return item_counts.get(item, 0)
    def update_count(item, new_quantity):
        if not isinstance(new_quantity, int) or new_quantity < 0:
            return False
        if item in item_counts:
            item_counts[item] = new_quantity
            return True
        return False
    def display_counts():
        print("--- Current Item Counts ---")
        for item, count in item_counts.items():
            print(f"{item}: {count}")
        print("---------------------------")
    print("Initial State:")
    display_counts()
    print("\n--- Testing Add Operation ---")
    add_item("apple", 5)
    add_item("grape", 10)
    add_item("apple", 3)
    display_counts()
    print("\n--- Testing Get Operation ---")
    print(f"Count of banana: {get_count('banana')}")
    print(f"Count of kiwi (non-existent): {get_count('kiwi')}")
    print("\n--- Testing Update Operation ---")
    update_count("banana", 50)
    update_count("kiwi", 5)
    print(f"Count of banana after update: {get_count('banana')}")
    print(f"Count of kiwi after update: {get_count('kiwi')}")
    print("\nFinal State:")
    display_counts()
if __name__ == '__main__':
    manage_item_counts()