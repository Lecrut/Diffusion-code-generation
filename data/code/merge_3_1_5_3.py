def extract_weights(record):
    """
    Recursively traverses a nested dictionary structure representing weight records
    and extracts all numerical weight values (integers or floats).
    
    Args:
        record: A dictionary containing weight data, potentially nested.
        
    Returns:
        A list of numbers found in the dictionary at any depth.
    """
    weights = []
    
    if isinstance(record, dict):
        for value in record.values():
            weights.extend(extract_weights(value))
            
    elif isinstance(record, (int, float)):
        # If we encounter a number directly, add it to the list
        weights.append(record)
        
    return weights

if __name__ == '__main__':
    # Hard-coded sample data representing nested weight records
    sample_data = {
        "patient_01": 75.5,
        "measurements": [
            {"date": "2023-01", "weight": 76.0},
            {"date": "2023-02", "weight": 74.8}
        ],
        "patient_02": {
            "notes": "Regular checkup",
            "record": [
                {"type": "start", "val": 65},
                {"type": "end", "value": 130.0}
            ]
        },
        "final_avg_weight": 78.2
    }

    result = extract_weights(sample_data)
    
    # Print the extracted weights for verification
    print("Extracted weight values:")
    for i, w in enumerate(result):
        print(f"Value {i + 1}: {w}")