#!/usr/bin/env python3
"""
Module: sort_objects_by_key

This module provides a utility to sort a list of dictionaries based on 
the value of a specified key in ascending order using the built-in `sorted()` function 
with a lambda expression for the key argument.
"""

def sort_dict_list(data, target_key):
    """
    Sorts a list of dictionaries by the values associated with 'target_key'.

    Args:
        data (list[dict]): A list containing dictionary objects to be sorted.
        target_key (str): The specific key within each dictionary used for sorting.

    Returns:
        list[dict]: A new list containing the same dictionaries, ordered by 
                    the values of 'target_key' in ascending order.
    
    Raises:
        TypeError: If data is not a list or if target_key is not a string.
        KeyError:   If any dictionary lacks the specified key (optional behavior, handled here to avoid runtime crash).
    """
    # Basic input validation
    if not isinstance(data, list):
        raise TypeError(f"Expected 'list', got {type(data).__name__}")
    
    if not isinstance(target_key, str):
        raise TypeError(f"Expected 'str' for key name, got {type(target_key).__name__}")

    # Check that all dictionaries contain the target key. 
    # If a missing key is found, we handle it gracefully by skipping or raising.
    # For production readiness without crashing on bad data in some contexts:
    if any(not isinstance(d, dict) for d in data):
        raise TypeError("All elements in 'data' must be dictionaries.")

    try:
        return sorted(data, key=lambda item: float(item.get(target_key))) 
    except (TypeError, ValueError) as e:
        # Fallback to string comparison if values are not all numeric floats
        return sorted(data, key=lambda item: str(item.get(target_key)))

if __name__ == '__main__':
    sample_data = [
        {"price": 150.20, "item": "Apple"},
        {"price": 349.99, "item": "Laptop"},
        {"price": 75.00, "item": "Banana"},
        {"name": "Coffee", "size": 5}, # This will cause a KeyError if we don't handle missing keys in the lambda logic gracefully 
    ]

    # Correcting sample data to ensure 'value' key exists for demonstration of numeric sorting.
    corrected_data = [
        {"price": 100, "name": "Item A"},
        {"price": 50, "name": "Item B"},
        {"price": 200, "name": "Item C"},
        {"price": 75.5, "name": "Item D"}
    ]

    target_key = 'price'

    # Perform sorting using the lambda key as requested. 
    sorted_items = sort_dict_list(corrected_data, target_key)

    print("Original List:")
    for item in corrected_data:
        print(f"  {item}")

    print("\nSorted List (Ascending by price):")
    for item in sorted_items:
        print(f"  {item}")