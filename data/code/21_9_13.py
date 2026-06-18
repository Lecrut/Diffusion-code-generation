def sort_objects_by_key(objects: list[dict], key_name: str) -> list[dict]:
    """
    Sort a list of dictionaries in ascending order based on the value 
    associated with a specific key using the sorted() function and lambda.
    
    Args:
        objects (list[dict]): List of dictionary objects to sort.
        key_name (str): The string name of the key within each object to use for sorting.
        
    Returns:
        list[dict]: A new list containing the same dictionaries, sorted by the specified key in ascending order.
    """
    return sorted(objects, key=lambda obj: obj.get(key_name))

if __name__ == '__main__':
    # Hard-coded sample data
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "Diana", "age": 29}
    ]

    # Sort the list by 'age' in ascending order
    sorted_people = sort_objects_by_key(people, key_name="age")

    print("Sorted people by age:")
    for person in sorted_people:
        print(f"{person['name']}: {person['age']} years old")