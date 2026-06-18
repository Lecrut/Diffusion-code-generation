def sort_objects_by_key(objects: list[dict], key_name: str) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value of a specified key in ascending order.
    
    Args:
        objects (list): A list of dictionary objects to be sorted.
        key_name (str): The name of the key within each dictionary used for sorting.
        
    Returns:
        list: A new list containing the dictionaries sorted by the specified key.
            
    Raises:
        KeyError: If a dictionary in the list does not contain the specified key.
    
    Example usage:
        data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        sorted_data = sort_objects_by_key(data, 'age')
    """
    return sorted(objects, key=lambda item: item.get(key_name))

if __name__ == '__main__':
    # Hard-coded sample data without user input or external dependencies
    sample_data = [
        {'id': 103, 'product': 'Laptop', 'price': 999.5},
        {'id': 102, 'product': 'Mouse', 'price': 25.0},
        {'id': 104, 'product': 'Keyboard', 'price': 75.0},
        {'id': 101, 'product': 'Monitor', 'price': 350.0}
    ]

    # Define the key to sort by (e.g., price)
    target_key = "price"

    if not sample_data:
        print("Input list is empty.")
    else:
        sorted_list = sort_objects_by_key(sample_data, target_key)
        
        print(f"Original data:")
        for item in sample_data:
            print(item)
            
        print("\nSorted data (by price):")
        for item in sorted_list:
            print(item)