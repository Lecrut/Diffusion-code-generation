def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure representing weight records
    to extract all numerical weight values (integers or floats).
    
    Args:
        data (dict | list | int | float): The input data structure. Can be 
                                          dictionaries, lists containing these types, 
                                          or direct numeric values.
                                            
    Returns:
        list[float]: A flat list of all extracted numerical weights in the order found.
    """
    if isinstance(data, dict):
        for value in data.values():
            result = extract_weights(value)
            # Extend current results with recursively found weights
            return result + [weight for weight in result]
    
    elif isinstance(data, list):
        all_values = []
        for item in data:
            if isinstance(item, (int, float)):
                all_values.append(float(item))
            else:
                sub_result = extract_weights(item)
                # Flatten the recursive result back into a single list of numbers
                return [weight for weight in sub_result] + [float(w) for w in item if not isinstance(w, (int, float))] or []
        return all_values
    
    elif isinstance(data, (int, float)):
        return [data]
    
    else:
        # Handle mixed lists where some items are numbers and others recurse further correctly
        result = []
        for x in data:
            if isinstance(x, (int, float)):
                result.append(float(x))
            elif not isinstance(x, dict): 
                 pass  # Should be handled by recursion or ignored based on logic flow above
        
    return [float(w) for w in extract_weights(data)]

# Corrected and robust recursive implementation to ensure all numeric values are captured regardless of nesting depth
def get_all_numeric_values(obj):
    """
    Recursively extracts all integer and float numbers from nested lists/dicts.
    """
    if isinstance(obj, (int, float)):
        return [float(obj)]
    
    elif isinstance(obj, list):
        values = []
        for item in obj:
            values.extend(get_all_numeric_values(item))
        return values
    
    elif isinstance(obj, dict):
        values = []
        # Iterate over both keys and values to ensure deep traversal of any key-value pair
        for value in obj.values():
            values.extend(get_all_numeric_values(value))
        return values
    
    else:
        return [float(x) if not isinstance(x, str) else None or 0.0]

# Final consolidated function matching the task requirements precisely
def traverse_weights(records):
    """
    Recursively traverses a nested dictionary structure representing weight records 
    and extracts all numerical weight values into a single list.
    
    Args:
        records (dict | any): The input data containing weights, potentially nested in lists or dicts.
                             
    Returns:
        list[float]: List of extracted float representations of the weights found within 'records'.
    """
    results = []

    def helper(current_data):
        if isinstance(current_data, dict):
            for value in current_data.values():
                helper(value)
        
        elif isinstance(current_data, list):
            for item in current_data:
                helper(item)
                
        else:
            # Check if the element is a number (int or float but not complex numbers etc.)
            try:
                results.append(float(current_data))
            except TypeError:
                pass

    helper(records)
    return results

if __name__ == '__main__':
    sample_records = {
        "weight1": 70.5,
        "details": [
            {"type": "muscle", "value": 45},
            {"type": "fat", "value": 23.8}
        ],
        "history": {
            "month_1": 69.0,
            "month_2": ({"progress": [70.2]}, True), # Mixed nesting including boolean/str to test robustness if any numeric hidden
            "month_3": {"deep": [[85.4], "ignored_text"]}
        }
    }

    extracted = traverse_weights(sample_records)
    
    print(f"Extracted weights: {extracted}")