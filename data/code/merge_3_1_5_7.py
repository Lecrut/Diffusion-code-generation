def extract_weights(nested_dict):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        nested_dict (dict or any): The input data structure containing weights.
        
    Returns:
        list[float]: A list of all extracted float/numeric weight values.
    """
    if isinstance(nested_dict, dict):
        result = []
        for value in nested_dict.values():
            result.extend(extract_weights(value))
    elif isinstance(nested_dict, (int, float)):
        # Ensure we only add numeric weights and not integers that might represent years or counts.
        # Given the task context of "weight records", any number is technically a candidate, 
        # but typically weight implies positive floats or ints associated with metrics.
        # We will include all numbers found as per standard recursive extraction logic for this problem type.
        result.append(float(nested_dict))
    else:
        pass
    
    return result

if __name__ == '__main__':
    sample_data = {
        "person_1": 70.5,
        "activities": {
            "running": {"distance_km": 5, "weight_kg": 68.2},
            "cycling": {"duration_minutes": 30} # This is not a weight but part of the structure to test recursion depth if mixed types existed (though only numbers are extracted)
        },
        "person_2": {
            "height_cm": 175,
            "weight_kg": 82.4,
            "details": {"gear_weight_g": 100} # Mixed unit scale but still a number
        }
    }

    weights = extract_weights(sample_data)
    
    print("Extracted weight values:")
    for w in sorted(weights):
        print(f"{w:.2f}")