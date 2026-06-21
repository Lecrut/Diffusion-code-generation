def check_elements_in_list(primary_list, secondary_list):
    if not isinstance(primary_list, list) or not isinstance(secondary_list, list):
        raise ValueError("Both inputs must be lists.")
    
    primary_set = set(primary_list)
    secondary_set = set(secondary_list)
    
    return bool(secondary_set & primary_set)

if __name__ == '__main__':
    sample_primary_list = [10, 25, 37, 42, 50]
    sample_secondary_list = [37, 60, 75]
    
    result = check_elements_in_list(sample_primary_list, sample_secondary_list)
    print(f"Primary List: {sample_primary_list}")
    print(f"Secondary List: {sample_secondary_list}")
    print(f"Do any elements from the secondary list exist in the primary list? {result}")