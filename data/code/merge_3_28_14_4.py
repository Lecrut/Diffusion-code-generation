class NumberSorter:
    """A class designed to store a numeric value and provide sorting-related methods."""

    def __init__(self, initial_value):
        """
        Initialize the NumberSorter with an integer or float value.

        Args:
            initial_value (int | float): The starting numerical value.
        
        Raises:
            TypeError: If the provided value is not a number.
        """
        if isinstance(initial_value, (int, float)):
            self.value = int(float(initial_value))  # Normalize to integer for consistency
        else:
            raise TypeError("The initial_value must be an integer or a numeric string/float.")

    def is_greater_than(self, other_value):
        """
        Checks if the object's internal value is larger than `other_value`.

        Args:
            other_value (int | float | Comparable): The value to compare against.

        Returns:
            bool: True if self.value > other_value, False otherwise.
        
        Raises:
            TypeError: If `other_value` cannot be compared with integers/floats.
        """
        try:
            return self.value > other_value
        except TypeError as e:
            raise TypeError(f"Cannot compare {type(self.value)} to type of '{other_value}'.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    sorter_instance = NumberSorter(105)

    test_cases = [
        90,      # Expected: False (105 > 90 is True? Wait logic check: "is greater than other", so self.value should be GREATER. 
                 # If comparing 105 vs 90 -> 105 > 90 is True.)
        120,     # Expected: False (105 <= 120)
        105,     # Expected: False (Equal returns False for strictly greater than)
    ]

    print("Testing NumberSorter.is_greater_than():")
    print(f"Internal value: {sorter_instance.value}\n")

    for test_val in test_cases:
        result = sorter_instance.is_greater_than(test_val)