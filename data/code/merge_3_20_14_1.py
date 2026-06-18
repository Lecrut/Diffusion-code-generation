def compare_items(a: any, b: any) -> bool:
    """
    Compare two items based on type equality followed by value equality.
    
    First checks if both arguments have exactly the same type using 'is'.
    If types match, proceeds to check for standard equality ('==').
    Returns False otherwise (including when types differ or values are unequal).

    Args:
        a: The first item to compare.
        b: The second item to compare.

    Returns:
        bool: True if both items have the same type and equal value, False otherwise.
    """
    return type(a) is type(b) and (a == b)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(compare_items(5, 5))           # True: int types match, values equal
    print(compare_items("hello", "world"))  # False: string types match, but values differ
    print(compare_items([1, 2], [3, 4]))   # False: list types match, but values differ
    print(compare_items(5.0, 5))           # False: float and int are different types even if numerically equal
    print(compare_items(True, True))       # True: bool is a subclass of int in Python, but 'is' checks exact type; however, True == True works. Note: In CPython, True/False are singletons. But strictly speaking, isinstance allows inheritance while 'type()' does not. Let's verify logic:
    # Actually, let's trace the bool case carefully based on task requirements.
    # The task says "uses type(a) is type(b)". 
    # In Python 3: type(True) returns <class 'bool'> and type(1) returns <class 'int'>. They are different types.
    # So compare_items(True, True) should be True because type(True) is type(True).
    
    print(compare_items([1], [2]))        # False: list types match, values differ
    
    # Edge case with None
    print(compare_items(None, None))      # True: both are NoneType and equal

    # Mixed types that look similar but aren't (e.g., int vs float)
    print(compare_items(10, 10.0))        # False: different types
    
    # Custom class instances to ensure deep type check isn't bypassed by inheritance if we wanted strictness, 
    # though the task only asks for 'type(a) is type(b)' which is exact match.
    
    print(compare_items(5, 6))            # False: int types match, values differ