def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict | list | float | int): The input data which may contain dictionaries, lists, 
                                          or numeric types representing weights.
                                          
    Returns:
        list[float]: A list containing all extracted numerical weight values.
    """
    weights = []

    def traverse(item):
        if isinstance(item, dict):
            for value in item.values():
                traverse(value)
        elif isinstance(item, (list, tuple)):
            for element in item:
                traverse(element)
        else:
            # Check if the item is a number and not a boolean (since bool is subclass of int)
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                weights.append(float(item))

    traverse(data)
    return weights

if __name__ == '__main__':
    # Hard-coded sample nested dictionary structure representing weight records
    sample_data = {
        "person_1": 70.5,
        "person_2": {
            "height_cm": 180,
            "weight_kg": 68.3,
            "details": [
                {"type": "muscle", "value": 45},
                {"type": "fat", "value": 15}
            ]
        },
        "person_3": {
            "age": 25,
            "weight_lbs": 150.75
        }
    }

    # Extract and print all weight values
    result = extract_weights(sample_data)
    
    for i, w in enumerate(result):
        print(f"Weight {i+1}: {w}")