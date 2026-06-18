def sort_objects_by_key(objects: list[dict], key_name: str) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value of a specific key in ascending order.
    
    Args:
        objects (list[dict]): The list of dictionary objects to be sorted.
        key_name (str): The name of the key within each dictionary that determines the sort order.
        
    Returns:
        list[dict]: A new list containing the sorted dictionaries.
    """
    return sorted(objects, key=lambda item: item.get(key_name))

if __name__ == '__main__':
    # Sample data block - no user input required
    sample_data = [
        {'id': 3, 'value': 'Charlie'},
        {'id': 1, 'value': 'Alice'},
        {'id': 2, 'value': 'Bob'}
    ]

    key_to_sort_by = 'value'

    sorted_result = sort_objects_by_key(sample_data, key_to_sort_by)

    # Output the result for verification (no interactive prompts used)
    print("Sorted list:")
    for item in sorted_result:
        print(item)