class Comparator:
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            a (any): First object to compare.
            b (any): Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing the check_equality method
    comparator = Comparator()

    test_cases = [
        (5, 5),           # Integers should be equal
        ("hello", "world"), # Strings not equal
        ([1, 2], [3, 4]), # Lists with different contents not equal
        ({'a': 1}, {'b': 1}), # Dictionaries with different keys not equal
        (True, False),    # Booleans not equal
        ("", ""),         # Empty strings are equal
        ([], []),         # Empty lists are equal
        (None, None),     # Both None should be considered equal by ==
    ]

    print("Running equality checks...")
    for i, (a, b) in enumerate(test_cases):
        result = comparator.check_equality(a, b)
        status = "Equal" if result else "Not Equal"
        print(f"Test {i+1}: check_equality({repr(a)}, {repr(b)}) -> {status}")

    # Additional test with objects that define custom __eq__
    class CustomObj:
        def __init__(self, value):
            self.value = value
        
        def __eq__(self, other):
            return isinstance(other, CustomObj) and self.value == other.value
    
    obj1 = CustomObj(42)
    obj2 = CustomObj(42)
    obj3 = CustomObj(99)

    print("\nCustom object tests:")
    result_custom_equal = comparator.check_equality(obj1, obj2)
    result_custom_not_equal = comparator.check_equality(obj1, obj3)
    
    if result_custom_equal:
        print(f"check_equality(CustomObj(42), CustomObj(42)) -> Equal")
    else:
        print("Error: Expected custom objects with same value to be equal.")

    if not result_custom_not_equal:
        print(f"check_equality(CustomObj(42), CustomObj(99)) -> Not Equal")
    else:
        print("Error: Expected custom objects with different values to be unequal.")