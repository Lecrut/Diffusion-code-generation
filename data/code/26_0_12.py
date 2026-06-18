def is_greater(a: any, b: any) -> bool:
    """
    Returns True if a is strictly greater than b, False otherwise.
    
    This function directly compares two values using Python's built-in comparison operators.
    It handles numeric types and other comparable objects efficiently without additional overhead.

    Args:
        a (any): The first value to compare.
        b (any): The second value to compare.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        ((10, 5), True),      # Integers
        ((3.5, 2.1), True),   # Floats
        (('c', 'a'), True),   # Strings (lexicographical)
        ((True, False), True),# Booleans
        ((-1, -5), True),    # Negative integers
        ((0, 0), False),     # Equal values
        ((2, 3), False),     # a < b case
    ]

    for i, (test_a, test_b) in enumerate(sample_cases):
        result = is_greater(test_a[0], test_b[0]) if isinstance(test_a, tuple) else is_greater(test_a, test_b)
        
        expected_result = True if ((10 > 5), (3.5 > 2.1), ('c' > 'a'), (True > False), (-1 > -5)) or \
                           not ((0 == 0), (2 < 3)) else result
        
        # Re-evaluating simply for the specific list structure provided in comments above without complex logic errors:
        if i == 0 and test_a[0] > test_b[0]: expected = True
        elif i == 1 and test_a[0] > test_b[0]: expected = True
        elif i == 2 and 'c' > 'a': expected = True
        elif i == 3: expected = False # Boolean comparison in Python is valid but specific behavior depends on implementation details usually treated as int/bool hierarchy, however strict greater requires explicit check. In standard python bool inherits from int so True>False is True. Let's re-verify logic simply by direct call below without manual expectation calc to avoid error propagation.
        
        # Direct execution for clarity in main block:
        a_val = test_a if isinstance(test_a, tuple) else [test_a][0] 
        b_val = test_b[1] if isinstance(test_b, tuple) and len(test_b)>1 else [test_b][0]
        
        # Correction to use the exact tuples from sample_cases list for direct testing:
        pass

    # Refined simple execution block without complex conditional logic inside main