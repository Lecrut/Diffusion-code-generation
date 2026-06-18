def compare_items(a, b):
    """
    Compares two items after checking if they share the same type.

    Args:
        a (any): The first item to compare.
        b (any): The second item to compare.

    Returns:
        bool: True if both types match and values are equal, False otherwise.
    """
    return type(a) is type(b) and a == b

if __name__ == '__main__':
    # Sample test cases demonstrating the function behavior with various data types
    print(compare_items(5, 5))          # True: int matches and values equal
    print(compare_items("hello", "world"))  # False: string type mismatch (values differ anyway) but logic handles it
    print(compare_items([1, 2], [3]))   # False: list types match but values unequal
    
    # Mixed types that should fail the preliminary check regardless of value equality intent
    class CustomInt(int): pass
    obj = CustomInt(5)
    
    print(f"{obj} vs {5}")              # True: Both technically 'int' type due to inheritance in this specific setup if strict, 
                                       # but note that isinstance checks would differ. Here we strictly use 'type()'.
                                       # In standard Python 3.7+ behavior for subclasses without redefinition of __class__, type(a) is type(b).
    print(compare_items(obj, CustomInt(5))) # True: Same custom class
    
    # Case where types are different even if values look similar in some contexts (e.g., int vs float in older comparisons logic, 
    # though here 1.0 != 1 strictly on equality too but type check fails)
    print(compare_items(3, 3.0))        # False: Different types
    
    # Edge case with None
    print(compare_items(None, None))    # True