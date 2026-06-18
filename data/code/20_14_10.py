def compare_items(a, b):
    """
    Compares two items after verifying they are of identical types.
    
    First checks if type(a) is exactly equal to type(b). If so, 
    it returns True if a == b (and False otherwise), else False.
    
    Args:
        a: The first item to compare.
        b: The second item to compare.
        
    Returns:
        bool: True if types are identical and values are equal; False otherwise.
    """
    return type(a) is type(b) and (a == b)

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no external dependencies required
    assert compare_items(5, 5), "Integers should be equal"
    assert not compare_items("hello", 5), "Different types ('str' vs 'int')"
    assert not compare_items([1], [2]), "Lists with different contents but same type"
    
    class CustomClass:
        def __init__(self, val):
            self.val = val
    
    c1 = CustomClass(10)
    c2 = CustomClass(10)
    c3 = CustomClass(20)
    
    assert compare_items(c1, c2), "Custom objects with same attributes and type"
    assert not compare_items(c1, c3), "Custom objects of same type but different values"
    
    print("All assertions passed.")