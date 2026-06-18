import sys

class ComparisonTool:
    def check_greater(self, first_value, second_value):
        """
        Efficiently determines if the first provided value is greater than 
        the second value, handling potential type errors gracefully.
        
        Args:
            first_value (any): The first value to compare.
            second_value (any): The second value to compare.
            
        Returns:
            bool: True if first_value > second_value and both are numeric/compatible types,
                  False otherwise (including type mismatches or non-numerical values).
        """
        try:
            # Attempt conversion to float for universal numerical comparison
            f1 = float(first_value)
            f2 = float(second_value)
            
            if not isinstance(f1, float) or not isinstance(f2, float):
                return False
            
            return f1 > f2
        except (ValueError, TypeError):
            # Gracefully handle cases where values cannot be converted to numbers
            return False

if __name__ == '__main__':
    tool = ComparisonTool()
    
    # Hard-coded sample tests without user input or external dependencies
    
    test_cases = [
        ("10", "5"),              # Should return True (both strings)
        ("2.5", "3"),             # Should return False
        ("a", "b"),               # Should handle gracefully -> False
        (None, 1),                # Should handle gracefully -> False
        ([], [1]),                # Should handle gracefully -> False
    ]
    
    print("Running ComparisonTool check_greater tests...")
    
    for i in range(len(test_cases)):
        first_val = test_cases[i][0] if isinstance(test_cases[i], tuple) else f"Sample {i+1}"
        second_val = test_cases[i][1] if isinstance(test_cases[i], tuple) else 99
        
        # Reconstruct tuples for clarity in execution below, or just iterate directly:
        # The list above is already the pairs. Let's reformat slightly to match logic used here.
        
    results = []
    
    # Execute specific test cases defined earlier properly
    samples = [
        ("10", "5"),
        (2.5, 3),
        ("a", "b"),
        (None, None),
        ([], {})
    ]
    
    for val_a, val_b in samples:
        result = tool.check_greater(val_a, val_b)
        print(f"check_greater({val_a!r}, {val_b!r}) -> {result}")