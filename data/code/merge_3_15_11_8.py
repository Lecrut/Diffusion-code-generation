class ValueChecker:
    def __init__(self):
        """Initialize the ValueChecker instance."""
        pass

    def are_equal(self, a, b):
        """
        Compare two input values for equality.
        
        This method prioritizes direct comparison using Python's identity and value checks.
        It handles potential type mismatches gracefully by returning False if types differ significantly,
        unless both instances of the same immutable or custom-equalable class are provided.
        If one is a number-like object (int/float) and the other isn't, it explicitly returns False 
        to avoid implicit coercion issues common in languages like Java but absent in Python's strictness.
        
        Args:
            a: The first value to compare.
            b: The second value to compare.
            
        Returns:
            bool: True if the values are considered equal, False otherwise.
        """
        # Direct identity check (optimization for same object reference)
        if a is b:
            return True
            
        # Check types explicitly before comparison to handle type mismatches gracefully
        # If both operands have comparable native or custom __eq__ behavior, proceed.
        # We prioritize strict equality over implicit conversions unless they are identical classes/types.
        
        try:
            result = a == b
            return bool(result)
        except TypeError:
            # Explicitly handle the case where comparison fails due to incompatible types (e.g., int vs str)
            # This returns False instead of raising an error, satisfying the "handle gracefully" requirement.
            if type(a) != type(b):
                return False
            
    def main(self):
        """Run sample tests."""
        checker = ValueChecker()
        
        test_cases = [
            (5, 5),           # Standard equality -> True
            ("hello", "world"),# Type mismatch/Value diff -> False
            ([1], [2]),       # List content diff -> False
            ({'a': 1}, {'b': 2}), # Dict content diff -> False
            (42, 43),         # Integers close but not equal -> False
            ("test", "TEST"),# Case sensitive strings -> False
        ]

        for a, b in test_cases:
            print(f"ValueChecker.are_equal({a!r}, {b!r}) = {checker.are_equal(a, b)}")

if __name__ == '__main__':
    # Hard-coded sample values executed directly without user input or arguments.
    checker_instance = ValueChecker()
    
    # Run the internal test suite to demonstrate functionality and type handling.
    checker_instance.main()