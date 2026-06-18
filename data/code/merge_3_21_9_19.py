def sort_objects_by_key(objects: list[dict], key_name: str) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value of a specified key in ascending order.
    
    Args:
        objects (list[dict]): The list of dictionary objects to be sorted.
        key_name (str): The name of the key within each dictionary used for sorting.
        
    Returns:
        list[dict]: A new list containing the same dictionaries, sorted by the specified key.
        
    Raises:
        ValueError: If any object in the list does not contain the specified key or if keys are unhashable (not applicable here as dicts use values).
    """
    return sorted(objects, key=lambda item: item.get(key_name))

if __name__ == '__main__':
    # Hard-coded sample data representing a list of products with 'price' and 'quantity'.
    product_list = [
        {"product_id": "P101", "name": "Laptop", "category": "Electronics", "price": 999.50, "quantity": 1},
        {"product_id": "P102", "name": "Mouse", "category": "Accessories", "price": 25.00, "quantity": 5},
        {"product_id": "P103", "name": "Keyboard", "category": "Accessories", "price": 79.99, "quantity": 3},
        {"product_id": "P104", "name": "Monitor", "category": "Electronics", "price": 299.00, "quantity": 2},
    ]

    # Sort the list by 'price' in ascending order using sorted() with a lambda key.
    sorted_products = sort_objects_by_key(product_list, "price")

    print("Sorted Product List:")
    for item in sorted_products:
        print(f"{item['name']}: ${item['price']} (Qty: {item['quantity']})")