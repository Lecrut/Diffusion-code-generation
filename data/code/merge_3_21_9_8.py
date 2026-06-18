def sort_objects_by_key(data: list[dict], key_name: str) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value associated with a specific key in ascending order.
    
    Args:
        data (list[dict]): The list of objects to be sorted.
        key_name (str): The name of the dictionary key to use as the sorting criterion.
        
    Returns:
        list[dict]: A new list containing the same dictionaries, but ordered by the specified key value in ascending order.
    
    Raises:
        ValueError: If any item in the data is not a dictionary or if the key_name does not exist in one of the items.
    """
    # Validate input types and keys to ensure robustness before sorting
    for i, obj in enumerate(data):
        if not isinstance(obj, dict):
            raise ValueError(f"Item at index {i} is not a dictionary.")
        if key_name not in obj:
            raise ValueError(f"Key '{key_name}' does not exist in item(s) of the list.")

    # Use sorted() with a lambda function to extract values for comparison and sort in ascending order.
    return sorted(data, key=lambda x: x.get(key_name))

if __name__ == '__main__':
    # Hard-coded sample data containing dictionaries representing users with an 'age' field.
    user_data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25},
        {"id": 3, "name": "Charlie", "age": 35},
        {"id": 4, "name": "David", "age": 25}
    ]

    # Define the key to sort by. In this case, it is 'age'.
    sort_key = 'age'

    try:
        sorted_users = sort_objects_by_key(user_data, sort_key)
        
        print("Sorted list of users by age:")
        for user in sorted_users:
            print(f"ID: {user['id']}, Name: {user['name']}, Age: {user['age']}")
    except ValueError as e:
        # Handle potential validation errors gracefully during execution.
        print(f"Error occurred while processing data: {e}")