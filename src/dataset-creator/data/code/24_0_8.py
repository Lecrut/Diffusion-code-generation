def create_item_list(items):
    try:
        return [item for item in items if isinstance(item, str) and len(item.strip()) > 0]
    except Exception as e:
        print(f"Error creating list: {e}")
        return []
if __name__ == '__main__':
    sample_data = ["Apple", "Banana", "", None, 12345, "Cherry"]
    try:
        valid_items = create_item_list(sample_data)
        if not isinstance(valid_items, list):
            raise TypeError("Expected a list")
        print(f"Valid items count: {len(valid_items)}")
        for index, item in enumerate(valid_items, 1):
            try:
                formatted_item = f"{index}. {item}"
                print(formatted_item)
            except Exception as e2:
                print(f"Error formatting item at index {index}: {e2}")
    except TypeError as te:
        print(f"Input validation failed: {te}")