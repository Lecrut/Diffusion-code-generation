def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if two items are strictly equal (value-wise), handling various data types correctly.
    
    Parameters:
        item1 (any): The first object to compare.
        item2 (any): The second object to compare.
        
    Returns:
        bool: True if the objects are deeply equal, False otherwise.
    
    Examples:
        >>> are_equal(5, 6)
        False
        >>> are_equal([1], [2])
        False
    """
    return item1 == item2

if __name__ == '__main__':
    pass
