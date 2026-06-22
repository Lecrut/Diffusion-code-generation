MAX_INDEX_ERROR = "Index out of range"
INVALID_TYPE_ERROR = "Invalid index type"

def print_element_at_index(lst, index):
    try:
        if not isinstance(index, int):
            raise ValueError(INVALID_TYPE_ERROR)
        if index < 0 or index >= len(lst):
            raise IndexError(MAX_INDEX_ERROR)
        element = lst[index]
        print(element)
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 10
    non_integer_index = 'a'
    
    print("Valid index example:")
    print_element_at_index(sample_list, valid_index)
    
    print("\nInvalid index example:")
    print_element_at_index(sample_list, invalid_index)
    
    print("\nNon-integer index example:")
    print_element_at_index(sample_list, non_integer_index)