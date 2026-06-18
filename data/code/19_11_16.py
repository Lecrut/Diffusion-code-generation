def is_condition_true(a: object, b: object) -> bool:
    """
    Returns True if a equals b (using '=='), otherwise False.
    Optimized by using Python's native comparison which handles references efficiently for immutable types 
    and delegates to appropriate logic for others without overhead from custom implementations.
    
    Args:
        a (object): First operand.
        b (object): Second operand.
        
    Returns:
        bool: True if a == b, False otherwise.
    """
    return a == b

if __name__ == '__main__':
    # Sample test cases with no user input or external dependencies
    
    # Test 1: Two integers are equal
    assert is_condition_true(5, 5) is True
    
    # Test 2: Two different integers are not equal
    assert is_condition_true(3, 7) is False
    
    # Test 3: List references (same object) -> equal by value in logic but same id usually; here we use == semantics
    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    assert is_condition_true(l1, l2) is True
    
    # Test 4: Dictionary references (different content structure but equal keys/values logically checked by )
    d1 = {'a': 1}
    d2 = {'b': 0.5}
    assert is_condition_true(d1, d2) is False

    print("All tests passed.")