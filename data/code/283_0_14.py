def are_elements_unique(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    
    seen = set()
    for item in lst:
        if not isinstance(item, (int, float)):
            raise ValueError("List elements must be integers or floats")
        
        if item in seen:
            return False
        seen.add(item)
    
    return True

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(are_elements_unique(sample_list))
    sample_list_with_duplicates = [1, 2, 3, 3, 5]
    print(are_elements_unique(sample_list_with_duplicates))