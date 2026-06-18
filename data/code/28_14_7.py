class NumberSorter:
    def __init__(self, initial_value):
        """Initialize the sorter with a specific numerical value."""
        self._value = initial_value
    
    @property
    def value(self) -> float | int:
        """Return the internal value of the sorter."""
        return self._value

    def is_greater_than(self, other_value) -> bool:
        """Check if this object's internal value is strictly greater than another value.
        
        Args:
            other_value (float | int): The value to compare against.
            
        Returns:
            bool: True if self._value > other_value, False otherwise.
        """
        return self.value > other_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sorter = NumberSorter(10)

    test_cases = [5, 10, 15]

    print(f"Testing with initial value: {sorter.value}")

    results = []
    for val in test_cases:
        is_greater = sorter.is_greater_than(val)
        results.append((val, is_greater))