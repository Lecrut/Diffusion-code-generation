def contains_element(primary_list, secondary_list):
    if not isinstance(primary_list, list) or not isinstance(secondary_list, list):
        raise ValueError("Both arguments must be lists.")
    
    primary_set = set(primary_list)
    return any(item in primary_set for item in secondary_list)

if __name__ == '__main__':
    sample_primary_list = [10, 25, 37, 42, 50]
    sample_secondary_list = [37, 60, 75]
    
    result = contains_element(sample_primary_list, sample_secondary_list)
    print(f"Primary List: {sample_primary_list}")
    print(f"Secondary List: {sample_secondary_list}")
    print(f"Does any element from the secondary list exist in the primary list? {result}")