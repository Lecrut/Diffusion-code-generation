def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict | list | float): The input structure containing weights and potential nesting.
        
    Returns:
        list[float]: A flat list of all extracted numerical weight values.
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
    sample_data = {
        "record_1": 70.5,
        "details": [
            {"id": 101, "weight": 68},
            {"id": 102, "notes": "Training", "weights": [69.2, 71.0]},
            {"id": 103}
        ],
        "record_2": {
            "name": "John",
            "weight": 85.4,
            "history": [[{"date": "2023-01"}, 67], [69]]
        }
    }

    result = extract_weights(sample_data)
    
    print("Extracted weights:")
    for w in result:
        print(f"{w}")