class NumberSorter:
    def __init__(self, value):
        """Initialize the sorter with a numeric value."""
        self.value = value
    
    def is_greater_than(self, other_value):
        """Check if this object's internal value is greater than another value.
        
        Args:
            other_value (int or float): The value to compare against.
            
        Returns:
            bool: True if self.value > other_value, False otherwise.
        """
        return self.value > other_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sorter = NumberSorter(10)
    
    test_cases = [5, 10, 20]
    
    print("Testing is_greater_than method:")
    for val in test_cases:
        result = sorter.is_greater_than(val)
        print(f"Is {sorter.value} greater than {val}? {result}")