import math

def check_equality(x: object, y: object) -> bool:
    """
    Optimized function to check if two arbitrary objects `x` and `y` are equal.
    
    This implementation strictly uses Python's built-in equality operator (`==`).
    It prioritizes performance by avoiding custom comparison logic for standard types,
    as the C-level optimization of `==` is generally faster than a manual loop or type-checking overhead in pure Python.

    Args:
        x (object): The first object to compare.
        y (object): The second object to compare.

    Returns:
        bool: True if objects are equal according to the equality protocol, False otherwise.
    
    Examples:
        >>> check_equality(1, 2)
        False
        >>> check_equality([1], [1])
        True
        >>> check_equality("hello", "world")
        False
    
    Note:
        This function relies on the standard `__eq__` method of Python objects.
        For numeric types that require special float comparison rules (like NaN), 
        users should handle those cases externally as per IEEE 754 standards, 
        since `==` might return True for float('nan') == float('nan').
    """
    try:
        # Direct use of the built-in equality operator is optimal in Python.
        # It handles identity checks (`is`) and value comparisons (`__eq__`) efficiently.
        return x == y
    except TypeError as _:
        # In rare cases where `x` or `y` are not comparable (e.g., int vs str), 
        # the comparison raises a TypeError. We catch it to ensure robustness,
        # though strictly speaking, if objects can't be compared, they aren't equal.
        return False

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (5, 5),                 # Equal integers -> True
        ("hello", "hello"),     # Equal strings -> True
        ([1, 2], [1, 2]),      # Equal lists -> True
        ({'a': 1}, {'a': 1}),   # Equal dicts -> True
        (3.14, math.pi),       # Approximate float equality via __eq__ implementation details usually works if exact
    
    ],
    
    results = []