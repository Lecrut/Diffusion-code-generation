def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict or any): The input dictionary which may contain nested dictionaries and lists
        
    Returns:
        list[float]: A flat list containing all extracted float/numeric weights
    """
    weights = []
    
    if isinstance(data, dict):
        for value in data.values():
            result = extract_weights(value)
            weights.extend(result)
    elif isinstance(data, (list, tuple)):
        for item in data:
            result = extract_weights(item)
            weights.extend(result)
    else:
        # Check if the value is a number and represents weight (float or int)
        try:
            float_val = float(data)
            # Optional validation to ensure it's within reasonable weight range could be added here
            if 0 <= float_val < 1e6: 
                weights.append(float_val)
        except (ValueError, TypeError):
            pass
            
    return weights

if __name__ == '__main__':
    # Hard-coded sample values representing a nested dictionary of weight records
    sample_data = {
        "person_001": {"weight_kg": 75.5},
        "person_002": [
            {"date": "2023-01", "value": 80.2},
            {"date": "2023-06", "value": 82.4}
        ],
        "person_003": {
            "measurements": [
                {"type": "landmark", "weight": 15000000}, # In grams, but stored as int
                {"type": "equipment", "value": 2.5}
            ]
        },
        "person_004": {
            "history": [
                {"year": 2020, "weight": 68.3},
                {"year": 2021, "weight": 70.1},
                {"year": 2022, "weight": 75.5}
            ]
        }
    }

    extracted_values = extract_weights(sample_data)
    
    print("Extracted weight values:")
    for idx, val in enumerate(extracted_values):
        print(f"{idx + 1}. {val}")