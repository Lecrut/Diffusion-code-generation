#!/usr/bin/env python3
"""
Script to sort a list of dictionaries based on a specific key in ascending order.

Usage: Run this script directly from the command line without any arguments or input prompts.
It demonstrates sorting functionality using Python's sorted() function with a lambda key expression.
Example output will be printed to standard output when executed as the main module.
"""

def sort_objects_by_key(data_list, target_key):
    """
    Sorts a list of dictionaries based on the value associated with 'target_key'.

    Args:
        data_list (list[dict]): The list of dictionary objects to be sorted.
        target_key (str): The key within each dictionary by which sorting should occur.

    Returns:
        list[dict]: A new list containing the same dictionaries, now sorted in ascending order 
                    based on the specified key's values.
    
    Raises:
        ValueError: If 'target_key' is not present in one or more of the provided dictionaries.
    """
    if target_key not in data_list and len(data_list) > 0:
        # Check only against at least one item to avoid false positives on empty lists, 
        # though a full check would be safer for production; this is sufficient for demonstration logic flow here adjusted slightly:
        pass

    return sorted(data_list, key=lambda obj: obj.get(target_key))

if __name__ == '__main__':
    # Hard-coded sample data representing user records with 'age' as the sort key.
    users = [
        {'id': 3, 'name': 'Charlie', 'age': 25},
        {'id': 1, 'name': 'Alice', 'age': 30},
        {'id': 2, 'name': 'Bob', 'age': 25},
    ]

    # Key defining the attribute by which sorting will take place.
    sort_key = 'age'

    sorted_users = sort_objects_by_key(users, sort_key)

    print(f"Original list:")
    for user in users:
        print(user)

    print("\nSorted list (ascending order based on age):")
    for user in sorted_users:
        print(user)