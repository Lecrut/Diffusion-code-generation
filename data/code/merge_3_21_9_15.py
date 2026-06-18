def sort_objects_by_key(objects: list[dict], key: str) -> list[dict]:
    """
    Sorts a list of dictionaries (objects) in ascending order based on 
    the value associated with a specific key using the sorted() function.

    Args:
        objects (list): A list of dictionary items to sort.
        key (str): The string key under which values should be extracted for sorting.

    Returns:
        list: A new list containing the same dictionaries, ordered by the specified key's value in ascending order.
    
    Raises:
        TypeError: If 'objects' is not a list or if any element in the list is not a dictionary.
        ValueError: If one of the keys referenced does not exist within all objects.
    """

    # Validate input type
    if not isinstance(objects, list):
        raise TypeError("The first argument must be a list.")

    for item in objects:
        if not isinstance(item, dict):
            raise TypeError(f"All elements in the list must be dictionaries. Found {type(item).__name__}.")

    # Check that all objects contain the specified key
    missing_keys = {}
    for obj in objects:
        if key not in obj:
            missing_keys[key] = f"missing from object with keys {list(obj.keys())}"

    if missing_keys:
        raise ValueError(f"The key '{key}' is required but missing from some objects:\n" + "\n".join([f"- {k}: {v}" for k, v in missing_keys.items()]))

    # Sort using the lambda function to access dictionary values by a specific string key
    sorted_objects = sorted(objects, key=lambda obj: obj[key])

    return sorted_objects

if __name__ == '__main__':
    sample_data = [
        {"age": 30, "city": "New York"},
        {"age": 25, "city": "London"},
        {"age": 45, "city": "Paris"},
        {"age": 25, "city": "Tokyo"}
    ]

    target_key = "age"
    
    try:
        result_list = sort_objects_by_key(sample_data, target_key)
        
        # Print the original list for comparison (optional but helpful for debugging in local runs without input prompts)
        print(f"Original List:")
        print([f"{item['city']} ({item['age']})" for item in sample_data])

        print("\nSorted List by age (ascending):")
        for item in result_list:
            print(f"{item['city']} ({item['age']})")

    except Exception as e:
        print(f"An error occurred during sorting: {e}")