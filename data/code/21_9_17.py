def sort_objects_by_key(objects: list[dict], key_name: str) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value associated with a specific key in ascending order.
    
    Args:
        objects (list[dict]): The list of dictionary objects to be sorted.
        key_name (str): The name of the key within each dictionary used for sorting.
        
    Returns:
        list[dict]: A new list containing the sorted dictionaries.
    """
    return sorted(objects, key=lambda item: item.get(key_name))

if __name__ == '__main__':
    # Hard-coded sample data representing a list of product objects with 'price' and 'quantity'.
    products = [
        {"id": 101, "product_name": "Laptop", "price": 999.50},
        {"id": 102, "product_name": "Mouse", "price": 25.00},
        {"id": 103, "product_name": "Keyboard", "price": 75.99},
        {"id": 104, "product_name": "Monitor", "price": 350.00}
    ]

    # Define the key to sort by (e.g., 'price')
    target_key = "price"

    # Perform the sorting operation using sorted() with a lambda function as the key argument.
    sorted_products = sort_objects_by_key(products, target_key)

    # Output the result directly without any user input prompts or interactive calls.
    print(f"Sorted list of {len(sorted_products)} products by '{target_key}' in ascending order:")
    for product in sorted_products:
        print(product)