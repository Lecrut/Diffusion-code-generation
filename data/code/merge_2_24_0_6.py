def create_item_list(items):
    try:
        return [item.strip() for item in items] if isinstance(items, list) else []
    except Exception as e:
        print(f"Error creating item list: {e}")
        return None
if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry"]
    try:
        valid_list = create_item_list(sample_items)
        if valid_list is not None and len(valid_list) > 0:
            print("Item List:")
            for i, item in enumerate(valid_list):
                print(f"{i + 1}. {item}")
        else:
            print("No items to display.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")