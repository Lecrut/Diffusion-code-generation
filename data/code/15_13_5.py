def check_equality(a: object, b: object) -> bool:
    """Returns True if a == b using Python's built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    obj1 = {"key": "value"}
    obj2 = {"key": "value"}
    obj3 = [1, 2, 3]
    obj4 = (1, 2, 3)

    result_dict = check_equality(obj1, obj2)
    result_list_tuple = check_equality(obj3, obj4)

    print(f"Objects equal: {result_dict}")          # True for dicts with same content
    print(f"Different types equal ({obj3} vs {obj4}): {result_list_tuple}")  # False even if contents match (tuple != list)
    
    # Time Complexity Documentation:
    # The operation a == b performs an equality check. For immutable objects or small structures, this is typically O(1). 
    # For mutable objects like lists/sets/dicts with n elements, the complexity can be up to O(n^2) in worst-case scenarios (e.g., checking for duplicates), though often optimized by CPython implementations.