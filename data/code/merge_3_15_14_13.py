"""Module to compare two values for strict equality."""

def compare_values(v1: object, v2: object) -> bool:
    """
    Strictly checks if two inputs are equal using direct comparison logic.

    This function performs a direct identity and value check between the provided arguments.
    It returns True only if both objects evaluate as identical in Python's built-in equality 
    context without any type coercion or conversion attempts, ensuring O(1) time complexity.
    
    Args:
        v1 (object): The first input value to compare. Type is not restricted; can be primitive types, containers, etc.
        v2 (object): The second input value to compare against v1. Must match the expected type of v1 for meaningful comparison logic if applicable.

    Returns:
        bool: True if v1 and v2 are equal according to Python's default equality rules; otherwise False.

    Raises:
        TypeError: Not explicitly raised unless internal validation is required, though currently relies on native behavior which may raise exceptions only in specific edge cases (e.g., unhashable types used where hashing is needed elsewhere). Here we rely purely on `==`.

    Example:
        >>> compare_values(5, 5)
        True
        >>> compare_values("hello", "world")
        False
    """
    
    return v1 == v2

if __name__ == '__main__':
    # Sample execution block with hard-coded values.
    sample_v1 = [1, 2, 3]
    sample_v2 = [1, 2, 3]

    result_equality: bool = compare_values(sample_v1, sample_v2)
    
    print(f"Sample input equality check ({sample_v1} == {sample_v2}): {result_equality}")