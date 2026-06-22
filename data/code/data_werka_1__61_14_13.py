def get_element(sequence, index):
    if not (0 <= index < len(sequence)):
        return None
    return sequence[index]

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    sample_tuple = ('a', 'b', 'c', 'd', 'e')
    
    index_to_retrieve = 3
    list_result = get_element(sample_list, index_to_retrieve)
    tuple_result = get_element(sample_tuple, index_to_retrieve)
    
    print(f"Element at index {index_to_retrieve} in the sample list: {list_result}")
    print(f"Element at index {index_to_retrieve} in the sample tuple: {tuple_result}")