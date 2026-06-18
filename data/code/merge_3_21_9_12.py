def sort_objects_by_key(objects: list[dict], key_name: str) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value of a specified key in ascending order.
    
    Args:
        objects (list[dict]): The list of dictionary objects to be sorted.
        key_name (str): The name of the key within each dictionary to use for sorting.
        
    Returns:
        list[dict]: A new list containing the same dictionaries, sorted by the specified key.
    
    Raises:
        ValueError: If any object in the list does not contain the specified key or if it's None.
    """
    # Validate that all objects have the required key and its value is comparable (not None)
    for obj in objects:
        if key_name not in obj or obj[key_name] is None:
            raise ValueError(f"All objects must contain a non-None '{key_name}' key.")

    return sorted(objects, key=lambda item: item.get(key_name))

if __name__ == '__main__':
    # Hard-coded sample data for testing without user input
    sample_data = [
        {"id": 3, "value": "Charlie"},
        {"id": 1, "value": "Alice"},
        {"id": 2, "value": "Bob"},
        {"id": 4, "value": "David"}
    ]

    # Define the key to sort by (using 'value' as an example)
    target_key = "value"

    try:
        sorted_data = sort_objects_by_key(sample_data, target_key)
        
        print("Sorted list:")
        for item in sorted_data:
            print(item)
            
    except ValueError as e:
        print(f"Error during sorting: {e}")