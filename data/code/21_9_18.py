def sort_objects_by_key(objects: list[dict], key_name: str) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value associated with a specific key in ascending order.
    
    Args:
        objects (list[dict]): The list of dictionary objects to be sorted.
        key_name (str): The string representing the key by which sorting should occur.
        
    Returns:
        list[dict]: A new list containing the same dictionaries, sorted according to the specified key.
    
    Raises:
        ValueError: If any object in the list does not contain the specified key.
    """
    if not objects or not isinstance(objects, list):
        raise TypeError("Input must be a non-empty list.")
        
    for obj in objects:
        if not isinstance(obj, dict) or key_name not in obj:
            raise ValueError(f"Object missing required key '{key_name}'.")

    return sorted(objects, key=lambda x: x[key_name])

if __name__ == '__main__':
    # Hard-coded sample data representing a list of product dictionaries.
    products = [
        {"id": 3, "name": "Laptop", "price": 1200},
        {"id": 1, "name": "Mouse", "price": 25},
        {"id": 2, "name": "Keyboard", "price": 75},
    ]

    # Define the key to sort by. In this case, 'price'.
    target_key = "price"

    try:
        sorted_products = sort_objects_by_key(products, target_key)
        
        print("Sorted products (by price):")
        for product in sorted_products:
            print(f"{product['name']}: ${product['price']}")
            
    except ValueError as e:
        print(f"Error during sorting: {e}")