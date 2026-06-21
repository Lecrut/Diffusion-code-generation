def print_element_at_index(lst, index):
    try:
        if not isinstance(lst, list):
            raise ValueError("The first argument must be a list.")
        if not isinstance(index, int):
            raise ValueError("The second argument must be an integer.")
        element = lst[index]
        print(element)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError:
        print("IndexError: Index is out of range.")

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    VALID_INDEX = 2
    INVALID_INDEX = 10
    NON_INTEGER_INDEX = 'a'
    
    print_element_at_index(SAMPLE_LIST, VALID_INDEX)
    print_element_at_index(SAMPLE_LIST, INVALID_INDEX)
    print_element_at_index(SAMPLE_LIST, NON_INTEGER_INDEX)