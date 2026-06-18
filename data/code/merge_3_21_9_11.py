#!/usr/bin/env python3
"""
Module to sort a list of dictionaries based on a specific key in ascending order.
Uses the `sorted()` function with a lambda as the key argument.
No external inputs, command-line arguments, or network access are required.
"""

def sort_objects_by_key(objects: list[dict], target_key: str) -> list[dict]:
    """
    Sorts a given list of dictionaries in ascending order based on the value 
    associated with `target_key`.

    Args:
        objects (list): A list of dictionary objects.
        target_key (str): The key within each dictionary to sort by.

    Returns:
        list[dict]: A new sorted list containing the original dictionaries.
    
    Raises:
        ValueError: If `target_key` is not found in one or more dictionaries, 
                   as it cannot determine a valid ordering for those items.
    """
    # Check if all objects contain the target key to ensure safe sorting
    missing_keys = [obj for obj in objects if target_key not in obj]
    
    if missing_keys:
        raise ValueError(f"Key '{target_key}' is missing from some dictionaries.")

    return sorted(objects, key=lambda item: item[target_key])

if __name__ == '__main__':
    # Hard-coded sample data representing a list of employee records.
    employees = [
        {"id": 301, "department": "Sales", "salary": 75000},
        {"id": 298, "department": "Engineering", "salary": 95000},
        {"id": 304, "department": "Marketing", "salary": 68000},
        {"id": 295, "department": "Sales", "salary": 71000}
    ]

    # Define the key to sort by. In this case, 'salary'.
    target_key = "salary"

    try:
        sorted_employees = sort_objects_by_key(employees, target_key)
        
        print("Sorted employees (by salary ascending):")
        for emp in sorted_employees:
            print(f"{emp['id']}: {emp['department']} - ${emp['salary']:,.0f}")

    except ValueError as e:
        print(f"Error during sorting: {e}")