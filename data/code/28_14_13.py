class NumberSorter:
    """A class designed for sorting operations with comparison capabilities."""

    def __init__(self, value):
        """Initialize the sorter with a numeric value."""
        self.value = value

    def is_greater_than(self, other_value):
        """Check if the object's internal value is larger than the provided other_value.

        Args:
            other_value (int or float): The value to compare against.

        Returns:
            bool: True if self.value > other_value, False otherwise.
        """
        return self.value > other_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sorter = NumberSorter(105)

    test_cases = [
        (90, True),      # 105 is greater than 90
        (200, False),    # 105 is not greater than 200
        (105, False),    # Not strictly greater than itself
        (-5, True),      # 105 is greater than negative number
    ]

    for test_input, expected_result in test_cases:
        result = sorter.is_greater_than(test_input)
        assert result == expected_result, f"Test failed for {test_input}: got {result}, expected {expected_result}"
    
    print("All tests passed.")