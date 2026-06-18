class NumberSorter:
    def __init__(self, value):
        """Initialize the sorter with a numeric value."""
        self.value = value
    
    def is_greater_than(self, other_value):
        """Check if this object's internal value is strictly greater than another value.
        
        Args:
            other_value (int | float): The value to compare against.
            
        Returns:
            bool: True if self.value > other_value, False otherwise.
        """
        return self.value > other_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    sorter1 = NumberSorter(25)
    result1a = sorter1.is_greater_than(10)
    result1b = sorter1.is_greater_than(30)

    print(f"Value: {sorter1.value}")
    print(f"Is 25 > 10? {result1a}")
    print(f"Is 25 > 30? {result1b}")

    # Test with second instance using float to ensure mixed type handling logic holds (Python handles it)
    sorter2 = NumberSorter(4.7)
    result2 = sorter2.is_greater_than(4.69)
    
    print(f"Value: {sorter2.value}")
    print(f"Is 4.7 > 4.69? {result2}")