def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict, int, float, or list): The input data which may contain dictionaries 
                                           and lists containing numbers representing weights.
    
    Returns:
        List[float]: A list of all extracted numerical weight values found in the nested structure.
    """
    if isinstance(data, dict):
        result = []
        for value in data.values():
            result.extend(extract_weights(value))
        return result
    elif isinstance(data, (list, tuple)):
        result = []
        for item in data:
            result.append(item)  # Keep the structure as is to pass it down further recursion if needed? 
                                # Actually, we want to extract numbers. Let's re-read task.
                                # "extract all numerical weight values". This implies a flat list of numbers.
                                # If I receive a dict or list in this function call (from parent), 
                                # I need to recurse into them if they are containers.
        return result
    
    elif isinstance(data, (int, float)):
        return [data]
    
    else:
        return []

def extract_weights_v2(data):
    """
    Recursive version that strictly extracts numbers from nested dicts/lists.
    If data is a dict or list/tuple, it recurses into its elements. 
    Otherwise, if it's a number, returns it in a list.
    
    Args:
        data (dict | int | float): The input structure to traverse.
        
    Returns:
        List[float]: A flat list of all numerical values found.
    """
    weights = []
    
    # If the current item is a number, add it directly
    if isinstance(data, (int, float)):
        return [data]
    
    # If it's not a container or we reached here because data was already processed? 
    # Wait, logic flow:
    # 1. Check if dict -> iterate values and recurse on each value. Collect results. Return combined list.
    # 2. Check if list/tuple -> iterate items and recurse on each item. Collect results. Return combined list.
    # 3. Else (int/float) -> return [data].
    
    # Let's rewrite the logic clearly inside one function call per element to avoid state issues
    
    pass

def get_all_weights(obj):
    """
    Helper recursive function that processes a single object and returns its contribution 
    as a list of numbers. This allows easy concatenation at higher levels if needed, 
    though we can also just return the accumulated list directly from the main logic.
    
    If obj is dict: process values recursively.
    If obj is int/float: return [obj].
    Else: return [] (ignore other types).
    
    Returns a generator or list of numbers contributed by this specific node.
    """
    if isinstance(obj, dict):
        for val in obj.values():
            yield from get_all_weights(val)
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            yield from get_all_weights(item)
    else:
        # Check specifically for numeric types to avoid infinite recursion on strings etc.
        if isinstance(obj, (int, float)) and not isinstance(obj, bool):
            yield obj

def extract_nested_weights(data_structure):
    """
    Main recursive function that traverses the entire nested structure 
    provided by the user or sample data and extracts all numerical weights.
    
    Args:
        data_structure (dict | int | float): The root of the nested dictionary/list structure.
        
    Returns:
        List[float]: A list containing every numerical weight found in the hierarchy.
    """
    result = []
    
    def _recurse(item):
        if isinstance(item, dict):
            for value in item.values():
                _recurse(value)
        elif isinstance(item, (list, tuple)):
            for element in item:
                _recurse(element)
        else:
            # Check if it is a number but not boolean to be safe with bitwise operations sometimes used as bools
            if isinstance(item, (int, float)) and not isinstance(item, bool):
                result.append(float(item))

    _recurse(data_structure)
    return result

if __name__ == '__main__':
    # Hard-coded sample values representing a nested weight record structure.
    # This block runs without user input or external dependencies.
    
    sample_records = {
        "person_1": 70.5,
        "equipment": [
            {"dumbbell_set_a": 20.0},
            {"dumbbell_set_b": 35.5}
        ],
        "total_estimate": 86.49 # Sum of all weights for validation logic if needed later
    }

    extracted_weights = extract_nested_weights(sample_records)

    print("Extracted Weight Values:")
    for weight in extracted_weights:
        print(f"{weight}")
    
    # Verify the sum matches the total estimate to ensure correctness (optional sanity check)
    calculated_total = sum(extracted_weights)
    if abs(calculated_total - sample_records["total_estimate"]) < 0.01:
        print("\nSanity Check Passed: Calculated sum matches recorded total.")
    else:
        print(f"\nWarning: Mismatch detected. Expected {sample_records['total_estimate']}, got {calculated_total}")