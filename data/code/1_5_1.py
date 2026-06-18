import json

def extract_weights(record):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        record (dict or any): A single element from the data structure, typically expected to be a dict 
                             at this level but may contain lists within it for robust traversal in similar structures.
        
    Returns:
        list[float]: A flat list containing all extracted numerical weight values as floats.
    """
    weights = []

    if isinstance(record, (int, float)) and not isinstance(record, bool):
        # If the record is a number, add it to the list
        weights.append(float(record))
    elif isinstance(record, dict):
        # Recursively process each value in the dictionary
        for value in record.values():
            weights.extend(extract_weights(value))
    elif isinstance(record, (list, tuple)):
        # Process items in lists or tuples if they exist as intermediate structures
        for item in record:
            weights.extend(extract_weights(item))

    return weights

if __name__ == '__main__':
    # Hard-coded sample values representing a nested dictionary structure of weight records
    sample_data = {
        "person_1": {
            "height_cm": 175,
            "weight_kg": 70.5,
            "details": [
                {"age": 30},
                {"mass_g": 82} # Mixed unit in nested detail
            ]
        },
        "person_2": {
            "height_cm": 160,
            "weight_kg": 55.2
        },
        "person_3": [
            {"name": "runner", "mass_lbs": 198}, # Mixed unit (lbs) - treated as weight anyway per prompt context or ignored if strictly kg? 
                                                    # Prompt asks for numerical values, so we include it to be safe.
            {10: "running_record"}
        ]
    }

    extracted_weights = extract_weights(sample_data)
    
    print("Extracted Weight Values:")
    print(extracted_weights)