def check_equality():
    """
    Compares two values based on both type equality and value equality.
    
    Args: None
    
    Returns: Boolean indicating if types match AND values match.
    """
    val1 = 42
    val2 = "42"

    # Check if the exact types are equal using direct comparison
    is_type_equal = type(val1) == type(val2)
    
    # If types are not exactly equal, they cannot be considered equal in this context.
    if not is_type_equal:
        return False
    
    # Since we prioritized exact type matching, the value check follows naturally 
    # for integers (and other immutable types). For floats or complex cases,
    # standard equality operators work after ensuring types are identical.
    is_value_equal = val1 == val2

    return is_type_equal and is_value_equal

if __name__ == '__main__':
    result = check_equality()
    print(f"Types match: {type(42) == type('42')}")  # Demonstrates the logic without input()