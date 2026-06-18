def decide_truth(val1: any, val2: any) -> bool:
    """
    Evaluates whether two arbitrary values are equal using Python's identity or value equality semantics.

    This function compares `val1` and `val2`. If they represent the same object (for immutable types 
    like numbers, strings, tuples of literals, etc., this usually means having identical content) it returns True;
    otherwise, it returns False. For mutable objects like lists or dicts, Python's default comparison checks for equality in terms of value and structure.

    Args:
        val1 (any): The first arbitrary value to compare.
        val2 (any): The second arbitrary value to compare.

    Returns:
        bool: True if `val1` is equal to `val2`, False otherwise.

    Examples:
        >>> decide_truth(5, 5)
        True
        
        >>> decide_truth("hello", "world")
        False
        
        >>> decide_truth([1, 2], [3, 4])
        False
    
    Note:
        The comparison logic is identical to the built-in `val1 == val2` expression. It handles all data types 
        supported by Python's equality operator without exception handling or type coercion beyond standard behavior.
    
    """
    return val1 == val2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality
    samples = [
        (42, 42),           # Integers should match
        ("text", "text"),   # Strings should match
        ([0.5], [0.5]),     # Lists with same float content
        ({'a': 1}, {'a': 1}),# Dictionaries with same key-value pairs
        (True, True),       # Booleans
        ((3,), (3,)),       # Tuples
    ]

    print("Running decide_truth function:")
    for i in range(0, len(samples), 2):
        val1 = samples[i]
        val2 = samples[i + 1] if i + 1 < len(samples) else None
        
        result = decide_truth(val1, val2)
        
        # Print the comparison and its boolean outcome
        print(f"decide_truth({val1!r}, {val2!r}) -> {result}")

    # Test a case that should return False for completeness in this block
    diff_result = decide_truth("different", "same")
    assert not diff_result, "Expected 'False' for different strings."
    
    print("\nAll internal tests passed.")