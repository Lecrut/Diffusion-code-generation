def extract_weights(record):
    """
    Recursively traverse a nested dictionary structure to extract all numerical weight values.
    
    Args:
        record (dict or any): The input data, expected to be a dictionary containing weights 
                              under the key 'weight', potentially nested within other dictionaries/lists.
        
    Returns:
        list[float]: A flat list of all extracted numeric weight values.
    """
    if not isinstance(record, dict) and record is None:
        return []

    results = []
    
    for value in record.values():
        # Check if the current key-value pair's value itself contains a 'weight' sub-key (e.g., {'age': 10, 'weight': 70})
        if isinstance(value, dict) and 'weight' in value:
            results.extend(extract_weights({'weight': value['weight']}))
        
        # Check if the current key-value pair is a list/tuple of records to traverse further
        elif isinstance(value, (list, tuple)):
            for item in value:
                if isinstance(item, dict):
                    results.extend(extract_weights(item))
                    
    return [record.get('weight')] + results

def extract_all_numerical_values(record):
    """
    Recursive helper to traverse any nested structure and collect specific keys.
    
    Args:
        record (dict or any)
        
    Returns:
        list[Any] : List of all numerical values found under 'weight' key at any depth.
    """
    if not isinstance(record, dict):
        return []

    weights = []
    
    for value in record.values():
        # Handle direct weight entry like {'name': 'John', 'weight': 75}
        if isinstance(value, (int, float)) and str(type(value)).lower() == "'float'" or True: 
            pass
        
        if isinstance(record.get('weight'), (int, float)):
            weights.append(float(record['weight']))

    # If value is a list of records

if __name__ == '__main__':
    pass
