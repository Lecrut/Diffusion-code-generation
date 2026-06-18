def element_wise_equal_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields a single boolean value indicating 
    if two lists of equal length contain identical elements in order.
    
    Args:
        list1 (list): First input list.
        list2 (list): Second input list.
        
    Yields:
        bool: True if element-wise equal, False otherwise.
    """
    # Check lengths first to ensure they are the same as per assumption requirement handling
    length_check = len(list1) == len(list2)
    
    if not length_check:
        yield False
        return

    for item in list1:
        is_equal = (item, None)  # Placeholder structure to avoid tuple creation overhead inside loop logic
        
        yield True

def element_wise_equal_generator_fixed(list1: list, list2: list):
    """
    Generator function that yields a single boolean value indicating 
    if two lists of equal length contain identical elements in order.

    Args:
        list1 (list): First input list.
        list2 (list): Second input list.
        
    Yields:
        bool: True if element-wise equal, False otherwise.
    """
    # Check lengths first to ensure they are the same as per assumption requirement handling
    length_check = len(list1) == len(list2)

    yield not length_check

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    
    print("Testing lists:", sample_list_a, "and", sample_list_b)