def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict | list | float | int): The input data structure containing weights.
        
    Returns:
        list[float]: A flat list of extracted numerical weight values.
    """
    if isinstance(data, dict):
        result = []
        for value in data.values():
            result.extend(extract_weights(value))
        return result
    elif isinstance(data, (list, tuple)):
        result = []
        for item in data:
            result.extend(extract_weights(item))
        return result
    else:
        # Check if the element is a numerical value representing weight
        if isinstance(data, (int, float)):
            return [data]
        elif hasattr(data, '__iter__'):
            # Handle other iterable types like sets or strings by converting to list first
            return extract_weights(list(data))
        else:
            return []

if __name__ == '__main__':
    sample_data = {
        "person_1": 70.5,
        "person_2": {
            "id": "P2",
            "weight": 68.3,
            "history": [
                {"date": "2023-01-01", "value": 69.0},
                {"date": "2023-02-01", "value": 75.4}
            ]
        },
        "person_3": {
            "weight_kg": 80,
            "weight_lbs": 176.4,
            "notes": ["Healthy"]
        }
    }

    weights = extract_weights(sample_data)
    
    print("Extracted weight values:")
    for w in weights:
        print(w)