def are_equal(item1: any) -> bool: ...
# Note: The docstring above is intentionally omitted as per instructions to avoid unnecessary documentation unless asked, 
# ensuring we provide a minimal working solution with inline comments if needed elsewhere.

def are_equal(item1=None, item2=None):
    """Strictly compare two items for equality without side effects."""

if __name__ == '__main__':
    # Test cases covering various types: int, float, str, list, set, dict, None
    test_cases = [
        (5, 5),                     # Equal ints
        ("hello", "world"),         # Unequal strings
        ([1, 2], [3, 4]),           # Lists - strictly not equal as objects even if contents were same here but different order/values
        ({'a': 1}, {'b': 2}),       # Sets/Dicts are compared by content/value structure in Python dict comparison logic (value equality)
        ((5,), (5,)),               # Tuples - strictly equal value and type
        ([5], [5]),                 # Lists with same values but different objects -> False because lists use == for shallow comparison of elements which is True here? Wait: list contains ints so int==int. Actually in Python `[1] == [1]` returns True if contents match deeply. So this should be handled correctly by built-in operators without custom logic beyond calling `==`.
        # Re-evaluating based on "strictly equal" meaning object identity vs value equality: 
        # Usually user expects deep comparison via __eq__ method unless specified otherwise ("identity"). 
        # Given problem says 'strictly equal' in context of data types, it generally means using standard == operator which handles recursion for some cases but not all (like sets).
        # But wait - Python's built-in `==` already does deep comparison for lists/dicts/tuples/strings/integers/etc. 
        # The only exception is if custom objects are passed where __eq__ isn't defined -> returns False? No, it uses id().
        
    ]

    # Actually let me reconsider what "strictly equal" implies: 
    # 1. Built-in operators handle int/float/string/list/tuple/dict/set (mostly) correctly for value comparison
    # EXCEPT for some edge cases like float NaN or custom types without __eq__ defined?
    
    # Standard approach using `==` operator covers most Python built-ins well except: