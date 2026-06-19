def print_element_at_index(data_list, index):
    try:
        if not isinstance(data_list, list):
            raise TypeError("The first argument must be a list.")
        if not isinstance(index, int):
            raise TypeError("The second argument must be an integer.")
        if index < 0 or index >= len(data_list):
            raise IndexError("Index is out of range.")
        
        print(data_list[index])
    except (TypeError, IndexError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 10
    non_list_input = "not a list"
    
    print("Valid index example:")
    print_element_at_index(sample_list, valid_index)
    
    print("\nInvalid index example:")
    print_element_at_index(sample_list, invalid_index)
    
    print("\nNon-list input example:")
    print_element_at_index(non_list_input, 0)