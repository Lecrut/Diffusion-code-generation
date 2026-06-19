def is_valid_index(sequence, index):
    return 0 <= index < len(sequence)

def get_element(sequence, index):
    if not is_valid_index(sequence, index):
        return None
    return sequence[index]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    sample_tuple = (10, 20, 30, 40, 50)
    
    index_to_retrieve = 3
    element_from_list = get_element(sample_list, index_to_retrieve)
    element_from_tuple = get_element(sample_tuple, index_to_retrieve)
    
    print(f"Element at index {index_to_retrieve} in the list: {element_from_list}")
    print(f"Element at index {index_to_retrieve} in the tuple: {element_from_tuple}")