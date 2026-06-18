def create_item_list():
    try:
        items = ["Laptop", "Mouse", "Keyboard"]
        return items
    except Exception as e:
        print(f"Error creating list: {e}")
        return []
def display_items(items):
    if not isinstance(items, list):
        raise TypeError("Items must be a list")
    try:
        for i, item in enumerate(items, 1):
            if not isinstance(item, str) or len(item.strip()) == 0:
                print(f"Warning: Invalid item at index {i}")
                continue
            print(f"{i}. {item.capitalize()}")
    except Exception as e:
        print(f"Error displaying items: {e}")
def main():
    try:
        sample_items = create_item_list()
        if not isinstance(sample_items, list):
            raise ValueError("Sample data is invalid")
        display_items(sample_items)
    except Exception as e:
        print(f"Fatal error in script execution: {e}")
if __name__ == '__main__':
    main()