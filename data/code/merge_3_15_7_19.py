def filter_identical_values(source_dict):
    """
    Creates a new dictionary containing only keys where the values 
    associated with 'key_a' and 'key_b' from the source dictionary match each other exactly (case-sensitive string equality).
    
    Parameters:
        source_dict (dict): The input dictionary to process. Must contain both 'key_a' and 'key_b'.
        
    Returns:
        dict: A new dictionary with keys matching a subset of original keys, where value['key_a'] == value['key_b'].
             If any key from the original is missing in source_dict or if either value doesn't exist for that entry's context, it won't be included.
    """
    target_keys = ['key_a', 'key_b']

if __name__ == '__main__':
    pass
