def compare_values(v1: any, v2: any) -> bool:
    """
    Strictly checks if two values are equal using Python's built-in equality operator.
    
    This function performs a direct comparison between the provided arguments without 
    performing type coercion or attempting to convert inputs into other data types unless 
    their explicit representation matches perfectly (e.g., list vs tuple, float precision).
    
    Parameters:
        v1 (any): The first value to compare. Can be any Python object supported by '=='.
        v2 (any): The second value to compare against the first argument.
        
    Returns:
        bool: True if v1 is strictly equal to v2, False otherwise.
    
    Complexity:
        Time Complexity: O(1) - Assumes direct comparison logic which does not depend on 
                        input size for most primitive and immutable types (lists/strings are handled 
                        by their internal hash/equality checks in CPython which often involve iteration but 
                        this function call itself is considered a single operation relative to the caller).
        Space Complexity: O(1) - No additional data structures are created.

    Examples:
        >>> compare_values(5, 5)
        True
        >>> compare_values([1], [1])
        True
        >>> compare_values("a", "b")
        False
        >>> compare_values(None, None)
        True
    """
    return v1 == v2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    samples = [
        (5, 5),              # Integers equal -> True
        ([1], [1]),          # Lists identical -> True
        ("hello", "world"),  # Strings different -> False
        (3.14, 3.14),       # Floats with same precision -> True
        ({'a': 1}, {'a': 1}),# Dicts identical content/order -> True
        (None, None),        # Both null -> True
        ([], []),            # Empty lists -> True
    ]

    for i, pair in enumerate(samples):
        v1, v2 = pair
        result = compare_values(v1, v2)
        print(f"Test {i+1}: compare_values({v1!r}, {v2!r}) == {result}")