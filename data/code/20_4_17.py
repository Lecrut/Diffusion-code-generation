def equal_lists_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields a single boolean value indicating 
    if two lists are element-wise equal and have the same length.
    
    Args:
        list1 (list): First input list.
        list2 (list): Second input list.
        
    Yields:
        bool: True if lists are identical, False otherwise.
    """
    # Check lengths first for efficiency before iterating
    len1 = len(list1)
    len2 = len(list2)
    
    if len1 != len2:
        yield False
        return
    
    # Iterate through elements to check equality

if __name__ == '__main__':
    pass
