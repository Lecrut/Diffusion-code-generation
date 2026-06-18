def extract_weights(record):
    """
    Recursively traverses a nested dictionary structure representing weight records
    and extracts all numerical weight values (integers or floats).
    
    Args:
        record (dict | list | int | float): The input data structure. Can be 
                                            a dict, list of dicts/lists, or numeric value.
                                            
    Returns:
        list[float]: A flat list containing all extracted weight values.
    """
    weights = []

    if isinstance(record, dict):
        for key, value in record.items():
            # Recursively process the value regardless of its type (dict, list, or number)
            found_weights = extract_weights(value)
            weights.extend(found_weights)
    
    elif isinstance(record, list):
        for item in record:
            found_weights = extract_weights(item)
            weights.extend(found_weights)
            
    else:
        # If it's not a dict or list and is numeric (int/float), add to results
        if isinstance(record, (int, float)):
            weights.append(float(record))

    return weights

if __name__ == '__main__':
    # Hard-coded sample values representing nested weight records
    sample_data = {
        "person_1": 70.5,
        "person_2": {
            "weight_kg": 68.0,
            "details": [
                {"exercise_weight": 45},
                {"equipment": "bench", "load": 30}
            ]
        },
        "group_a": ["team1", 72.3],
        "person_3": {
            "height_cm": 180, # Not a weight but part of the structure to test recursion depth
            "weight_lbs": 156.4
        }
    }

    result = extract_weights(sample_data)
    
    print("Extracted weights:", result)