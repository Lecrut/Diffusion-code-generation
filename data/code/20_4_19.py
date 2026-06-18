def equal_lists_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields a single boolean value indicating 
    if two lists are element-wise equal and have the same length.
    
    Args:
        list1 (list): First input list.
        list2 (list): Second input list.
        
    Yields:
        bool: True if lists are of equal length and all elements match, False otherwise.
    """
    # Check lengths first for efficiency before iteration
    if len(list1) != len(list2):
        yield False
        return
    
    # Iterate through both lists to check element-wise equality

if __name__ == '__main__':
    pass
