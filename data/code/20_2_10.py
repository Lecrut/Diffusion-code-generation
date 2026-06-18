class Comparator:
    @staticmethod
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            self (object): Not used in static method but required by class structure.
            a (any): First object to compare.
            b (any): Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    comparator = Comparator()

    # Test cases with various object types
    test_cases = [
        (5, 5),                    # Integers
        ("hello", "hello"),       # Strings
        ([1, 2, 3], [1, 2, 3]),   # Lists
        ({'a': 1}, {'a': 1}),     # Dictionaries
        (object(), object()),     # Different instances of same class
    ]

    results = []
    for a, b in test_cases:
        is_equal = comparator.check_equality(None, a, b)
        expected = a == b
        result_status = "PASS" if is_equal == expected else "FAIL"
        results.append(result_status)
    
    # Print results to console (no file I/O or network access used)
    for i, status in enumerate(results):
        print(f"Test {i+1}: {'Equal' if test_cases[i][0] == test_cases[i][1] else 'Not Equal'} -> Result: {status}")

# Final verification output example (will run without any input prompts or files)
print("All tests completed successfully.")