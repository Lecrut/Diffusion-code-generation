class NumberSorter:
    """A class designed to handle numeric sorting operations."""

    def __init__(self, value):
        """Initialize the sorter with a specific integer or float value."""
        self.value = value

    def is_greater_than(self, other_value):
        """Check if the object's internal value is larger than another value.

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
        (200, False),    # 105 is not greater than 200
        (105, False),    # Equal values are not strictly greater
        (-5, True)       # Negative numbers work correctly too
    ]

    for test_val, expected in test_cases:
        result = sorter.is_greater_than(test_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] is 105 greater than {test_val}? Result: {result}, Expected: {expected}")

    # Demonstrate usage in a simple sorting context logic (though the class itself doesn't sort)
    numbers = [3, 7, 2]
    max_num = max(numbers)
    sorter_check = NumberSorter(max_num)
    
    print(f"\nMax of {numbers} is {max_num}")
    for n in numbers:
        if sorter_check.is_greater_than(n):
            print(f"{max_num} > {n}: True")
        else:
            print(f"{max_num} > {n}: False")