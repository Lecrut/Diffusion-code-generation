class NumberSorter:
    def __init__(self, value):
        """Initialize the sorter with an internal numerical value."""
        self.value = value
    
    def is_greater_than(self, other_value):
        """Check if the object's internal value is strictly greater than another value.

        Args:
            other_value (int | float): The value to compare against.

        Returns:
            bool: True if self.value > other_value, False otherwise.
        """
        return self.value > other_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sorter = NumberSorter(105)

    test_cases = [
        (90, True),      # 105 is greater than 90
        (110, False),    # 105 is not greater than 110
        (105, False),    # 105 is equal to 105, so strictly greater returns false
        (-5, True),      # 105 is greater than negative number
        (float('inf'), False)  # Infinity cannot be exceeded by a finite float
    ]

    print(f"Testing NumberSorter with internal value: {sorter.value}")
    
    for test_val, expected in test_cases:
        result = sorter.is_greater_than(test_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"is_greater_than({test_val}): Expected {expected}, Got {result} -> {status}")