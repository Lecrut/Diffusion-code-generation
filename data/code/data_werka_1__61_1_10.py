def get_element_at_position(data_list, index):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list.")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index < 0 or index >= len(data_list):
        raise IndexError("Index out of bounds.")
    return data_list[index]

if __name__ == '__main__':
    sample_data = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(f"Sample Data: {sample_data}")
    
    try:
        index_to_retrieve = 2
        element_at_index = get_element_at_position(sample_data, index_to_retrieve)
        print(f"Element at index {index_to_retrieve}: {element_at_index}")
        
        index_to_retrieve = 0
        element_at_index = get_element_at_position(sample_data, index_to_retrieve)
        print(f"Element at index {index_to_retrieve}: {element_at_index}")
        
        index_to_retrieve = 4
        element_at_index = get_element_at_position(sample_data, index_to_retrieve)
        print(f"Element at index {index_to_retrieve}: {element_at_index}")
    except Exception as e:
        print(f"An error occurred: {e}")