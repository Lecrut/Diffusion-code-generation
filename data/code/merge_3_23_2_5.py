class ValueComparator:
    """A class that compares two values and returns a descriptive string."""

    def compare(self, val1, val2):
        """
        Compares two input values of any comparable type (numbers, strings).

        Args:
            val1: The first value to compare.
            val2: The second value to compare.

        Returns:
            A string indicating which value is greater, less, or if they are equal.
            Possible return messages: "val1 is greater than val2", 
                                      "val2 is greater than val1", 
                                      "values are equal".
            
        Raises:
            TypeError: If the values cannot be compared (e.g., incompatible types).
        """
        try:
            if val1 > val2:
                return f"{type(val1).__name__} '{val1}' is greater than {type(val2).__name__} '{val2}'"
            elif val2 > val1:
                return f"{type(val2).__name__} '{val2}' is greater than {type(val1).__name__} '{val1}'"
            else:
                return "values are equal"
        except TypeError as e:
            raise TypeError(f"Incompatible types for comparison: {e}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    comparator = ValueComparator()

    test_cases = [
        (10, 5),           # Integers
        ("apple", "banana"),  # Strings
        (3.14, 2.718),     # Floats
        (-10, -5),         # Negative integers
        ("hello", "world"),# Longer strings
    ]

    print("Value Comparison Results:\n")
    for val1, val2 in test_cases:
        result = comparator.compare(val1, val2)
        print(f"Comparing {val1} and {val2}:")
        print(result)
        print("-" * 40)

    # Additional edge case check (should raise TypeError if uncommented or used with incompatible types like int/str directly in a loop without try-except, 
    # but here we stick to comparable pairs. To demonstrate error handling capability conceptually:
    
    # Uncommenting the line below would trigger an exception which is expected behavior for mixed types not designed for comparison by default logic above (though Python usually handles it gracefully with TypeError).
    # This block remains commented as per strict execution requirements without crashing on valid comparable inputs.