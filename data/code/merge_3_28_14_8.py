class SortableValue:
    def __init__(self, value):
        """Initialize the Sorted Value object with an internal numeric value."""
        self.value = value

    def is_greater_than(self, other_value):
        """Check if the instance's internal value is strictly greater than another number.

        Args:
            other_value (int or float): The value to compare against.

        Returns:
            bool: True if self.value > other_value, False otherwise.
        """
        return self.value > other_value

if __name__ == '__main__':
    # Hard-coded sample values for testing the method execution without user input.
    obj1 = SortableValue(50)
    obj2 = SortableValue(75)

    print("Testing is_greater_than logic:")
    
    test_cases = [
        (obj1, 40),     # Expected: True
        (obj1, 60),     # Expected: False
        (obj2, 30),     # Expected: True
        (50, 50.0),     # Edge case equality -> Expected: False
    ]