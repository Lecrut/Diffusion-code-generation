def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict | list | int | float): The input data which may be a dict, list of dicts/lists, 
                                          or direct numeric weights.
    
    Returns:
        list[float]: A flat list containing all extracted numerical weight values.
    """
    weights = []

    if isinstance(data, dict):
        for value in data.values():
            weights.extend(extract_weights(value))
    elif isinstance(data, (list, tuple)):
        for item in data:
            weights.extend(extract_weights(item))
    else:
        # Check if the value is a number (int or float) and not None
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            weights.append(float(data))

    return weights

if __name__ == '__main__':
    sample_data = {
        "person_1": 70.5,
        "activities": [
            {"run": 8.2},
            {"cycle": 45.3}
        ],
        "person_2": {
            "weight_kg": 65.0,
            "details": ["info", "more_info"]
        },
        "extra_notes": None
    }

    result = extract_weights(sample_data)
    
    # Print the extracted weights to verify functionality without user input
    print("Extracted weight values:")
    for w in sorted(result):  # Sorting for consistent output order
        print(f"{w}")