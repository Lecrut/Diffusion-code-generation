def print_element_at_index(lst, index):
    if not isinstance(lst, list):
        raise TypeError("The first argument must be a list.")
    if not isinstance(index, int):
        raise TypeError("The second argument must be an integer.")
    if index < 0 or index >= len(lst):
        raise IndexError("Index is out of range.")
    print(lst[index])

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 10
    non_integer_index = 'a'
    
    try:
        print_element_at_index(sample_list, valid_index)
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        print_element_at_index(sample_list, invalid_index)
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        print_element_at_index(sample_list, non_integer_index)
    except Exception as e:
        print(f"Error: {e}")