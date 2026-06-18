def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict | list | float): The input data which may contain dictionaries, lists, or numbers.
        
    Returns:
        list[float]: A list containing all extracted numerical weights.
    """
    weights = []

    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weights(value))
    elif isinstance(data, (list, tuple)):
        for item in data:
            weights.extend(extract_weights(item))
    else:
        # Check if the element is a number (int or float) but not boolean
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            weights.append(float(data))

    return weights

if __name__ == '__main__':
    sample_records = {
        "person_1": 70.5,
        "person_2": {
            "id": 42,
            "weight": 68.3,
            "details": [
                {"type": "muscle", "value": True},
                {"type": "fat", "value": 12.5}
            ]
        },
        "person_3": {
            "name": "Alice",
            "weight_kg": 80,
            "history": [75.0, 76.2, 74.9]
        }
    }

    all_weights = extract_weights(sample_records)
    
    # Output the result directly to stdout as a list of floats
    print(all_weights)