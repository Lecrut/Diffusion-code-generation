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
    # Hard-coded sample values for testing without user input or external dependencies
    comparator = Comparator()

    test_cases = [
        (5, 5),           # Integers should be equal
        ("hello", "world"),  # Strings are not equal
        ([1, 2], [3, 4]),   # Lists with different contents are not equal
        ({'a': 1}, {'b': 1}), # Dictionaries with different keys/values are not equal
    ]

    for i in range(len(test_cases)):
        a = test_cases[i][0]
        b = test_cases[i][1]
        result = comparator.check_equality(a, b)
        print(f"Test {i+1}: check_equality({a}, {b}) == {result}")

    # Additional explicit tests for clarity
    assert comparator.check_equality(42, 42), "Integers should be equal"
    assert not comparator.check_equality("test", "data"), "Strings should differ"
    
    print("\nAll assertions passed.")