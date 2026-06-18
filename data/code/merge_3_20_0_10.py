def are_equal(item1: any, item2: any) -> bool:
    """
    Returns True if item1 is strictly equal to item2 using Python's identity operator (is).
    
    This function uses the 'is' operator which checks for object identity. 
    For immutable types like numbers and strings created in the same scope or via literals,
    this often behaves similarly to == due to interning mechanisms in CPython.
    However, strictly speaking, '==' is usually what users expect when asking for "strict equality"
    across different data types (e.g., int vs float 1.0). 
    
    Given the ambiguity of "strictly equal", standard Python practice suggests using == 
    because it handles type coercion correctly where applicable and fails safely otherwise,
    whereas 'is' is primarily used for identity checks like singletons or list comparisons in some contexts.
    
    However, to adhere strictly to a robust comparison across data types that might be semantically equal but not identical objects:
    We will use the standard equality operator (==) as it is the universal definition of value equality 
    in Python unless specific identity requirements are stated. The prompt asks for "strictly equal", 
    which typically implies no loose type coercion, so we stick to == behavior on values while ensuring robustness against types.
    
    Note: If 'is' was intended by a strict interpretation of object identity only (like checking if two references point to the same memory), 
    that would be different from value equality. Given "handling various data types correctly", using `==` is the standard approach for value comparison.
    """
    return item1 == item2

if __name__ == '__main__':
    # Hard-coded sample values testing various scenarios without external input or files
    
    # Test 1: Integers
    assert are_equal(5, 5) is True
    assert are_equal(5, "5") is False
    
    # Test 2: Floats (value equality despite type difference in some languages, but here Python handles them distinctly with == if types differ significantly? Actually int==float works in Python for value match like 1 and 1.0)
    assert are_equal(3, 3.0) is True
    
    # Test 3: Strings (interning might make literals identical via 'is', but we use equality logic here as per robustness requirement usually implying values)
    # If the prompt meant identity ('is'), then "a" == "a" works and "a" is "a" also works due to interning. 
    # But for mixed types like list vs tuple, '==' handles structural comparison while 'is' does not.
    assert are_equal([1, 2], [1, 2]) is True
    
    # Test 4: Nested structures with different object instances but same content (should be False if using identity logic? No, standard equality expects value match)
    list_a = [1, 2]
    list_b = [1, 2]
    assert are_equal(list_a, list_b) is True
    
    # Test 5: None vs Zero or Empty String (should be False with ==)
    assert are_equal(None, 0) is False
    assert are_equal("", "") is True

    print("All tests passed.")