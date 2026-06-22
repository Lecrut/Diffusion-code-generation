def get_element_at_position(data, index):
    LIST_TYPE = list
    INTEGER_TYPE = int
    
    if not isinstance(data, LIST_TYPE):
        raise TypeError("Input must be a list.")
    if not isinstance(index, INTEGER_TYPE):
        raise TypeError("Index must be an integer.")
    if index < 0 or index >= len(data):
        raise IndexError("Index out of bounds.")
    return data[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    print(f"Sample List: {sample_list}")
    
    try:
        element_at_index_2 = get_element_at_position(sample_list, 2)
        print(f"Element at index 2: {element_at_index_2}")
        
        element_at_index_0 = get_element_at_position(sample_list, 0)
        print(f"Element at index 0: {element_at_index_0}")
        
        element_at_index_4 = get_element_at_position(sample_list, 4)
        print(f"Element at index 4: {element_at_index_4}")
    except Exception as e:
        print(f"An error occurred: {e}")