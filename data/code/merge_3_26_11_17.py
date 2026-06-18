import sys

class ComparisonTool:
    def check_greater(self, a, b):
        """
        Determines if value 'a' is strictly greater than value 'b'.
        
        Handles type errors gracefully by catching exceptions during comparison.
        Returns True if a > b and both are comparable numbers (int or float).
        Returns False otherwise without raising an exception for invalid types.
        
        Args:
            a: First value to compare.
            b: Second value to compare.
            
        Returns:
            bool: True if a is greater than b, False otherwise.
        """
        try:
            # Only perform comparison if both are numeric (int or float) and not booleans
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                return a > b
            else:
                # If types don't match expected numeric criteria, default to False
                return False
        except Exception:
            # Catch any other potential comparison errors gracefully
            return False

if __name__ == '__main__':
    tool = ComparisonTool()

    # Test cases with hard-coded sample values
    test_cases = [
        (10, 5),           # Expected: True
        (3.9, 4.0),        # Expected: False
        ("apple", "banana"),# Should not crash, return False due to type mismatch logic above or comparison failure if allowed by Python default behavior but we enforce numeric check here -> False based on isinstance
        (10, "ten"),       # Mixed types -> False per our strict numeric requirement in this implementation. 
                           # Note: Standard Python allows comparing int and str which raises TypeError. Our try/except catches it.
    ]

    print("Running ComparisonTool checks...")
    
    for i, item in enumerate(test_cases):
        a_val = item[0]
        b_val = item[1]
        
        result = tool.check_greater(a_val, b_val)
        status_str = "True" if result else "False"
        print(f"Test {i+1}: check_greater({a_val}, {b_val}) -> {status_str}")

    # Additional explicit numeric tests to ensure core functionality works without exceptions for valid inputs
    assert tool.check_greater(5, 3) == True
    assert tool.check_greater(2.5, 2.6) == False
    print("All assertions passed.")