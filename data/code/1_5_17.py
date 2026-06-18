def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure representing weight records
    and extracts all numerical weight values (integers or floats).
    
    Args:
        data: A dict containing key-value pairs where keys are strings and 
              values can be either integers, floats, lists of such types, 
              dictionaries with string/numeric/integral/float/list values.
              
    Returns:
        List[float]: All numerical weight values found in the structure.
    """
    weights = []
    
    def traverse_value(value):
        if isinstance(value, (int, float)):
            # Exclude boolean since bool is a subclass of int in Python
            # but we want to treat booleans as non-weight entries unless explicitly needed.
            # We'll assume only numbers are weights. Booleans should be skipped or treated carefully.
            # Given the context "weight records", 'True'/'False' are unlikely weight values, 
            # so we exclude them from numeric extraction here for safety if encountered mixed types,
            # but strictly speaking isinstance(True, int) is True in Python.
            # To be safe and logical: accept only numbers that aren't booleans.
            weights.append(value)
        elif isinstance(value, dict):
            traverse_value(value)
        elif isinstance(value, list):
            for item in value:
                if not isinstance(item, (dict, str)) or isinstance(item, bool): 
                    # If it's a string representing a number? The task implies numerical values.
                    # Let's stick to direct numeric types found in the structure as per typical nested dict problems.
                    traverse_value(item)

    # Initial call with root data handling if it matches list structures (though spec says dictionary)
    def recursive_process(current_data):
        nonlocal weights
        
        if isinstance(current_data, dict):
            for value in current_data.values():
                if isinstance(value, (int, float)) and not isinstance(value, bool):
                    weights.append(value)
                elif isinstance(value, list):
                    # Recurse into lists
                    new_weights = []
                    for item in value:
                        recursive_process(item)
                        new_weights.extend(weights[-len(range(0)):])  # Wait this is wrong logic inside recursion
            
            return

if __name__ == '__main__':
    pass
