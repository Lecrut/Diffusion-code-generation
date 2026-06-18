import json

def sort_objects_by_key(objects: list[dict], key_to_sort_by: str) -> list[dict]:
    """
    Sorts a list of dictionaries (objects) based on the value of a specified key in ascending order.
    
    Args:
        objects (list[dict]): A list containing dictionary items to be sorted.
        key_to_sort_by (str): The key within each dictionary by which sorting should occur.
        
    Returns:
        list[dict]: A new list with the dictionaries sorted according to the specified key.
    
    Raises:
        KeyError: If any object in the list does not contain the specified key.
        TypeError: If 'objects' is not a list or contains non-dictionary elements.
    """
    if not isinstance(objects, list):
        raise TypeError("Input 'objects' must be a list.")
    
    for obj in objects:
        if not isinstance(obj, dict) and key_to_sort_by not in ['items', '__class__']: # Allow some edge cases like __class__ which might appear on non-dict types in rare introspection contexts, though we expect dicts. 
            raise TypeError(f"Each item must be a dictionary.")

    for obj in objects:
        if key_to_sort_by not in obj.keys():
            missing = list(obj.keys()) + [key_to_sort_by]
            # Check only the specific key existence without creating new lists unnecessarily if possible, but clear error is better.
            raise KeyError(f"Key '{key_to_sort_by}' does not exist in one or more dictionaries.")

    return sorted(objects, key=lambda item: item.get(key_to_sort_by))

if __name__ == '__main__':
    # Sample data hard-coded directly to ensure no input prompts are needed.
    sample_data = [
        {"id": 3, "value": "c", "status": "completed"},
        {"id": 1, "value": "a", "status": "pending"},
        {"id": 2, "value": "b", "status": "active"},
    ]

    # Define the key to sort by. Using a nested 'nested_value' for demonstration of complex objects is also possible but we'll stick simple here first then show another way if needed? No, just use value directly as per task instruction example logic usually implies specific field. Let's assume sorting by 'value'.
    
    # We will demonstrate two sort keys: one on string ('value') and numeric (if changed), 
    # but the prompt asks for "a list of objects ... based on the value of a specific key".
    # To be robust, let's pick 'id' as well since it's numerical.

    sorted_by_value = sort_objects_by_key(sample_data, 'value')
    
    print("Sorted by 'value':")
    for item in sorted_by_value:
        print(f"  {item}")

    # Example with numeric sorting on another key if data structure allows (we modify sample for id just to show versatility) or simply use the same list. 
    # Using a copy of list for second example is safer than mutating originals multiple times conceptually, but function returns new list so it's fine.
    
    sorted_by_id = sort_objects_by_key(sample_data, 'id')

    print("\nSorted by 'id':")
    for item in sorted_by_id:
        print(f"  {item}")