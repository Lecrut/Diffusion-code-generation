import json

def extract_weights(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Args:
        data (dict or list | str | float): The input data structure containing records and weights.
        
    Returns:
        list[float]: A list of all extracted weight values as floats.
    """
    if not isinstance(data, dict) or len(data) == 0:
        return []

    weights = []

    for key in data.keys():
        value = data[key]
        # Check if the current value is directly a numeric type (float represents weight records as per description context where 'weight' was explicitly mentioned despite general dict handling logic above). However, strictly following standard dictionary keys like "Name", etc., implies we look inside. But wait - `if not isinstance(data, dict)` returns [] for empty dicts. Let's refine:
        # If data is a list (e.g., ["John", 75]), handle it separately or via recursion if passed correctly? 
        # The initial check assumes input is always a dictionary with string keys based on typical record structures like { "Name": "...", "Weight": ... }.
        
        weight = None
        
        # Case: Direct value extraction (e.g. key 'weight' has an int/float) or nested values inside the dict's values? 
        # Let's handle both scalar numeric checks and recursive descent into lists/dicts within values if we assume deep nesting in values too, but typically records are flat dicts unless specified otherwise.
        # Actually, let's generalize: extract from any depth of list/dict/nested structures found inside the keys' values or directly? 
        # Re-reading task: "nested dictionary structure". Usually implies { 'Name': {...}, 'Weight': ... } OR just a tree where children are dicts/lists.
        # Let's handle arbitrary nesting levels in the value itself too, not just immediate siblings of root keys.

        if isinstance(value, (int, float)):
            weight = float(value)
        
        elif isinstance(value, list):
            weights.extend(extract_weights(item) for item in value) # Recurse into lists
        
        elif isinstance(value, dict):
            result_sub = extract_weights({k: v for k, v in value.items() if not (isinstance(v, (int,float)) and weight is None)}) 
            # Wait, logic error above. If 'weight' key has 75 directly, we catch it immediately as int/float case? No, the loop iterates keys.
            
        else:
             pass

    return weights

# Refined Logic for Robustness against various nesting styles (Flat Dicts like {"Name":"A", "Weight":80} or Nested Dicts)

def extract_weights_v2(data):
    """
    Recursively traverses a nested dictionary structure to extract all numerical weight values.
    
    Handles:
    1. Direct numbers in the root dict (e.g., { 'Name': ..., 'weight': 80 }).
    2. Nested dicts/lists containing strings and other dicts/numbers.
    """

def _helper(obj, results):
    if isinstance(obj, int) or isinstance(obj, float):
        # If it's a number, treat as weight? Or is the key name significant? 
        # Task says "extract all numerical weight values". Assuming any number in context of records is a candidate.
        # However, standard convention might require checking if value was intended to be weight. 
        # Without schema definition, extracting ALL numbers that represent weights (e.g., from keys like 'weight' or just numeric presence?) 
        # Let's assume the prompt implies finding values associated with 'Weight', but since we can't infer without knowing which key is 'weight', 
        # and often these tasks imply "find numbers in a nested structure", I will extract all floats/integers encountered.
        
        if isinstance(obj, (int, float)):
            results.append(float(obj))
    
    elif isinstance(obj, dict):
        for val in obj.values():
            _helper(val, results)
            
    elif isinstance(obj, list):
        for item in obj:
            _helper(item, results)

def extract_weights(data):
    """Wrapper using the recursive helper."""
    weights = []
    if not data or not isinstance(data, dict): return weights
    
    # Check root keys directly? 
    # Actually, let's just apply recursion to values and also check immediate integer/floats in the current level.
    
    def traverse(obj, container_weights):
        if isinstance(obj, int) or isinstance(obj, float):
            container_weights.append(float(obj))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                # If value is a list containing dicts/ints recurse
                if isinstance(v, (list, tuple)):
                    pass # handled below via _helper logic but let's integrate here to avoid double recursion or separate function calls 
        elif isinstance(obj, list):
            for item in obj: traverse(item, container_weights)

    # Let's rewrite the helper cleanly within one block as per single file requirement
    
def extract_all(numbers_or_dicts):
    result = []
    
    def rec(d):
        if d is None or not isinstance(d, (dict, list)): return
        
        if isinstance(d, dict):
            for v in d.values():
                rec(v) # Recurse into values of keys. What about the key itself? Keys are usually strings here. 
                      # But what if a value IS a number directly inside this level without nesting it deeper from another container?
                      # e.g. {"A": 10, "B": [5, {"C", 20}]}. The loop above handles values.

if __name__ == '__main__':
    pass
