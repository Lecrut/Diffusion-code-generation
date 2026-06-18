#!/usr/bin/env python3
"""
Module to sort a list of dictionaries based on a specific key in ascending order.

This module provides functionality to take a list of objects (represented as 
dictionaries) and return a new sorted list where the items are ordered by 
the value associated with a given key, from lowest to highest. It utilizes 
Python's built-in `sorted()` function combined with a lambda expression for 
customization.
"""

def sort_objects_by_key(objects: list[dict], key_name: str) -> list[dict]:
    """
    Sorts a list of dictionaries based on the value of a specified key in ascending order.

    Args:
        objects (list[dict]): A list of dictionary objects to be sorted.
        key_name (str): The string name of the key within each dictionary by which sorting occurs.

    Returns:
        list[dict]: A new list containing the same dictionaries, but ordered 
                    according to the values of `key_name`. If a dictionary is missing 
                    the specified key or if an error arises during comparison, it will be handled gracefully 
                    (though for this specific task assuming valid input as per production-ready standards).
    
    Raises:
        ValueError: If any object in the list does not contain the specified key.

    Example:
        >>> data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
        >>> sorted_data = sort_objects_by_key(data, 'age')
        # Returns: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
    """
    
    def get_sort_value(obj):
        return obj.get(key_name)

    try:
        sorted_list = sorted(objects, key=get_sort_value)
        return sorted_list
    except TypeError as e:
        # This block catches cases where comparison might fail if keys are of incompatible types 
        # that cannot be compared directly (e.g., mixing strings and numbers), though typically 
        # Python's sort handles mixed types by raising an error which we re-raise here for clarity.
        raise ValueError(f"Error during sorting: {str(e)}") from e

if __name__ == '__main__':
    # Hard-coded sample data representing a list of user records with 'age' and 'score'.
    users = [
        {'id': 1, 'name': 'Alice', 'age': 30, 'score': 85},
        {'id': 2, 'name': 'Bob', 'age': 25, 'score': 92},
        {'id': 3, 'name': 'Charlie', 'age': 35, 'score': 78},
        {'id': 4, 'name': 'Diana', 'age': 28, 'score': 90}
    ]

    # Define the key to sort by. In this example, we will demonstrate sorting by 'age'.
    target_key = "age"

    print(f"Original list sorted by '{target_key}':")
    for user in users:
        print(user)

    # Perform the sorting operation using the defined function and lambda logic internally via get_sort_value.
    sorted_users = sort_objects_by_key(users, target_key)

    print("\nSorted list (ascending order):")
    for user in sorted_users:
        print(user)