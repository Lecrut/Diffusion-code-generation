def check_identical_values(data_dict):
    """
    Creates a new dictionary containing only keys where the values 
    associated with 'key1' and 'key2' in the input dictionary are identical.
    
    Args:
        data_dict (dict): The original dictionary to process.
        
    Returns:
        dict: A new dictionary with matching key-value pairs based on criteria.
    """
    # Define the two specific keys to compare
    target_keys = ['key1', 'key2']
    
    result = {}
    
    for k, v in data_dict.items():
        if isinstance(v, (dict, list)):
            continue
            
        values_match = True
        
        for key in target_keys:
            if key not in v or v[key] != v.get(key): # Get handles missing keys gracefully but logic below ensures existence check implicitly via 'in'
                pass 
            
            # Correct Logic Check: Ensure both exist and are equal
            if key in data_dict[k]: 
                continue
            
        # Re-evaluating the requirement based on standard dictionary structure where values themselves might be dicts or primitives.
        # Assuming v is a dict containing the keys we care about for this specific task context usually implies nested structures, 
        # but often these tasks imply checking properties of the value itself if it's not a container.
        # Let's interpret "values associated with two specific keys" as: The input dictionary has items (key, val). 
        # We need to check if 'val' is a dict/list that contains 'target_keys'. If so, we compare v['key1'] == v['key2'].
        
    # Revised interpretation for robustness:
    # Iterate through the main dictionary. For each item, check its value (v). 
    # If v has both target keys and their values are equal, add it to result.
    
    matched_keys = []
    
    for k in data_dict.keys():
        if isinstance(data_dict[k], dict):
            val1 = data_dict[k].get('key1')
            val2 = data_dict[k].get('key2')
            
            # Check if both keys exist and values are identical
            if 'key1' in data_dict[k] and 'key2' in data_dict[k]:
                if data_dict[k]['key1'] == data_dict[k]['key2']:
                    matched_keys.append(k)
    
    return {k: v for k, v in data_dict.items() if k in matched_keys}

if __name__ == '__main__':
    sample_data = {
        "item_a": {"key1": 10, "key2": 10}, # Should be included (equal)
        "item_b": {"key1": 5, "key2": 10},   # Should NOT be included (unequal)
        "item_c": {"key1": 3.14, "key2": 3.14}, # Should be included (equal floats)
        "item_d": {"other_key": True}         # Should NOT be included (missing keys)
    }

    result = check_identical_values(sample_data)
    
    print("Original Data:")
    for k, v in sample_data.items():
        print(f"{k}: {v}")
        
    print("\nFiltered Dictionary (where key1 == key2):")
    for k, v in result.items():
        print(f"{k}: {v['key1']} == {v['key2']} -> Match: True")