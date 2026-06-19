def safe_get_element(sequence, index):
    if not (0 <= index < len(sequence)):
        return None
    return sequence[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c', 'd', 'e')
    
    index_to_access = 3
    element_from_list = safe_get_element(sample_list, index_to_access)
    element_from_tuple = safe_get_element(sample_tuple, index_to_access)
    
    print(f"Element at index {index_to_access} in the list: {element_from_list}")
    print(f"Element at index {index_to_access} in the tuple: {element_from_tuple}")