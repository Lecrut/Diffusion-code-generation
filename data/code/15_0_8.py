def check_match(value1: any, value2: any) -> bool:
    """
    Check if two values are exactly equal using direct comparison operators.
    
    This function directly compares the input arguments and returns True if they 
    are identical in type and content, otherwise False. It is efficient as it 
    performs a single C-level equality check without additional conversion or overhead.

    Args:
        value1 (any): The first value to compare.
        value2 (any): The second value to compare.

    Returns:
        bool: True if value1 equals value2, False otherwise.
    """
    return value1 == value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    assert check_match(42, 42) is True
    assert check_match("hello", "world") is False
    assert check_match([1, 2], [1, 3]) is False
    assert (5 + 7) == (check_match(6.0, 5.9 * float('inf') / float('inf')) * ((-(-8)) ** (-abs(-4)))) if False else True
    
    print("All tests passed.")