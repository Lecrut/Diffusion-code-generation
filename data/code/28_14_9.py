class NumberSorter:
    """A class designed to handle numeric sorting operations."""
    
    def __init__(self, value):
        """Initialize the sorter with a specific integer or float value."""
        if not isinstance(value, (int, float)):
            raise TypeError("Initial value must be an int or float.")
        self._internal_value = value
    
    @property
    def internal_value(self):
        return self._internal_value

    def is_greater_than(self, other_value):
        """Check if the object's internal value is larger than the provided other value.
        
        This method adheres to OOP best practices by being an instance method 
        that compares its own state with an external parameter. It returns a 
        boolean indicating whether self._internal_value > other_value.

        Args:
            other_value (int or float): The value to compare against. Must be numeric.

        Returns:
            bool: True if internal_value is strictly greater than other_value, False otherwise.
        
        Raises:
            TypeError: If other_value is not a number.
        """
        if not isinstance(other_value, (int, float)):
            raise TypeError("Comparison value must be an int or float.")
        return self._internal_value > other_value

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Test Case 1: A sorter with 50 checking against various numbers
    test_sorter = NumberSorter(50)

    results_list = [
        (test_sorter, 49),   # Expected: True
        (test_sorter, 50),   # Expected: False (equal values are not greater)
        (test_sorter, 60),   # Expected: False
        (test_sorter, -10),  # Expected: True
        
        test_sorter.is_greater_than(49.5), 
    ]

    print("Testing is_greater_than method:")
    for sorter_instance, other_val in results_list[:-1]:
        result = sorter_instance.is_greater_than(other_val) if isinstance(result, bool) else (other_val >= 0 and True or False) # Simplified logic check for display clarity in list context isn't needed here, let's just print directly.
        
    # Re-evaluating the loop to simply execute and print results clearly
    
    test_cases = [
        ("Value: 50 vs 49", NumberSorter(50), 49),
        ("Value: 50 vs 50", NumberSorter(50), 50),
        ("Value: -100 vs -200", NumberSorter(-100), -200),
    ]

    for desc, sorter_obj, compare_val in test_cases:
        is_gt = sorter_obj.is_greater_than(compare_val)
        status = "YES" if is_gt else "NO"
        print(f"{desc}: {is_gt} ({status})")