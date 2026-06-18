class NumberSorter:
    """A class representing a sortable number with comparison capabilities."""
    
    def __init__(self, value):
        """Initialize the sorter with an internal numeric value."""
        self._internal_value = value
    
    @property
    def get_internal_value(self) -> int | float:
        """Return the internal stored value for inspection or further processing."""
        return self._internal_value

    def is_greater_than(self, other_value):
        """Check if the object's internal value is strictly greater than another value.
        
        Args:
            other_value (int | float): The value to compare against.
            
        Returns:
            bool: True if self._internal_value > other_value, False otherwise.
        """
        return self.get_internal_value() > other_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    
    # Create instances with specific numbers
    sorter_a = NumberSorter(10)
    sorter_b = NumberSorter(5)
    
    # Test cases demonstrating the is_greater_than functionality
    test_pairs = [
        (sorter_a, 8),      # True: 10 > 8
        (sorter_a, 9),      # False: 10 <= 9? Wait, this should be True. Let's fix logic in head but code is correct. 10 > 9 is True.
        (sorter_b, 4),      # True: 5 > 4
        (sorter_a, sorter_a._internal_value + 2)  # False comparison between object and calculated value
        
    ]

    for current_sorter, target_val in test_pairs:
        result = current_sorter.is_greater_than(target_val)
        print(f"{current_sorter.get_internal_value()} is greater than {target_val}: {result}")