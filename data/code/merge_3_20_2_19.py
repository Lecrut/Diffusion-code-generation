class Comparator:
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            a (any): The first object to compare.
            b (any): The second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Sample values for testing the check_equality method without user input
    comparator = Comparator()

    test_cases = [
        (5, 5),           # Integers should be equal
        ("hello", "world"), # Strings should not be equal
        ([1, 2], [3, 4]), # Lists with different contents should not be equal
        ({'a': 1}, {'b': 2}), # Dictionaries with different keys/values
        (True, True),     # Booleans should be equal
        ((1+1), (2)),     # Arithmetic expressions evaluated before comparison
    ]

    for i, (obj_a, obj_b) in enumerate(test_cases):
        result = comparator.check_equality(obj_a, obj_b)
        print(f"Test case {i + 1}: check_equality({repr(obj_a)}, {repr(obj_b)}) -> {result}")