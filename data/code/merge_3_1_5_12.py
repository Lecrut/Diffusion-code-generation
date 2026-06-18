def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict | list | float | int): The input data which can be dictionaries, lists, numbers, or mixed types.
        
    Returns:
        list[float]: A flat list containing only the extracted numerical weights.
    """
    weights = []

    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weights(value))
    elif isinstance(data, (list, tuple)):
        for item in data:
            weights.extend(extract_weights(item))
    else:
        # Check if the current element is a numerical weight
        if isinstance(data, (int, float)):
            weights.append(float(data))

    return weights

if __name__ == '__main__':
    sample_data = {
        "record_1": 70.5,
        "details": {
            "height": 180,
            "weight_kg": 68.2,
            "equipment_weight": [5.0, 3.5],
            "notes": {"extra_load": 2.1}
        },
        "record_2": 75.0,
        "activities": {
            "running": {"weight_with_gear": 80},
            "cycling": [69.3, 4.2]
        }
    }

    weights_list = extract_weights(sample_data)
    
    print("Extracted weight values:")
    for w in sorted(weights_list):
        print(f"{w}")