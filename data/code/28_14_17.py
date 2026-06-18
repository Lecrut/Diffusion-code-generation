class NumberSorter:
    def __init__(self, value):
        """Initialize the sorter with a numeric value."""
        self.value = int(value) if isinstance(value, (str, float)) else value
    
    def is_greater_than(self, other_value):
        """Check if the internal value is strictly greater than another number.
        
        Args:
            other_value: The value to compare against. Can be an integer or float.
            
        Returns:
            bool: True if self.value > other_value, False otherwise.
        """
        return self.value > int(other_value)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sorter = NumberSorter(105)
    
    test_cases = [
        90,      # Should be False (105 is not greater than 90? Wait, 105 > 90 is True. Logic check: return self.value > other_value) -> True
        104,     # Should be True
        200,     # Should be False
    ]

    results = []
    for test_val in test_cases:
        res = sorter.is_greater_than(test_val)
        results.append(f"Is {sorter.value} greater than {test_val}? {res}")
    
    print("\n".join(results))