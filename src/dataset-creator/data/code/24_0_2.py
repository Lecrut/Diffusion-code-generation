def create_item_list(items):
    try:
        return [item for item in items if isinstance(item, str) and len(item.strip()) > 0]
    except Exception as e:
        print(f"Error creating list: {e}")
        return []
if __name__ == '__main__':
    sample_items = ["Apple", "Banana", "", None, "Cherry"]
    try:
        valid_list = create_item_list(sample_items)
        if not isinstance(valid_list, list):
            print("Error: Invalid return type from function")
        else:
            for index, item in enumerate(valid_list, 1):
                print(f"{index}. {item}")
    except Exception as e:
        print(f"Fatal error during execution: {e}")