#!/usr/bin/env python3
"""
Module to sort a list of dictionaries based on a specific key in ascending order.

This module provides functionality to take a list of objects (represented as 
dictionaries), identify a target key, and return a new sorted list without 
modifying the original data structure. The sorting is performed using Python's
built-in `sorted()` function with a lambda expression acting as the key extractor.

Usage:
    Run the module directly to see example usage with pre-defined sample data.
"""

def sort_objects_by_key(objects, target_key):
    """
    Sorts a list of dictionaries based on the value associated with a specific key.

    Args:
        objects (list[dict]): A list of dictionary objects. Each object should 
                              contain the `target_key`. If an item lacks this 
                              key or it is not hashable, sorting will raise a TypeError.
        target_key (str): The key name in each dictionary to use for sorting comparison.

    Returns:
        list[dict]: A new list containing the same dictionaries as input but sorted
                    by `target_key` in ascending order.
    
    Raises:
        KeyError: If any object in the list does not contain the specified `target_key`.
        TypeError: If the value associated with `target_key` is unhashable (e.g., a list).

    Examples:
        >>> data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
        >>> sort_objects_by_key(data, 'age')
        [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]

    Note:
        The original input list `objects` is not modified. A new sorted list 
        is returned to ensure immutability of the source data during operation.
    
    """
    # Validate that all items contain the target key before attempting sort
    for item in objects:
        if target_key not in item or isinstance(item[target_key], (list, dict)):
            raise TypeError(f"Cannot use '{target_key}' as a sorting key because " 
                           f"some values are unhashable.")

    # Use the built-in sorted function with a lambda to extract and compare keys.
    return sorted(objects, key=lambda item: item[target_key])

if __name__ == '__main__':
    # Hard-coded sample data representing a list of user objects.
    users = [
        {'id': 102, 'username': 'charlie', 'score': 85},
        {'id': 101, 'username': 'alice', 'score': 92},
        {'id': 103, 'username': 'bob', 'score': 76}
    ]

    # Define the key used for sorting (e.g., user score).
    sort_key = 'score'

    try:
        sorted_users = sort_objects_by_key(users, sort_key)
        
        print(f"Original List ({len(users)} items):")
        for u in users:
            print(f"  {u}")
            
        print("\nSorted List (Ascending by score):")
        for user in sorted_users:
            print(f"  {user}")

    except KeyError as e:
        # This block is unreachable given the input but included for completeness.
        raise Exception(f"A required key was not found: {e}") from None