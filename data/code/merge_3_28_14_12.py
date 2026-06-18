class NumberComparator:
    def __init__(self, value):
        """Initialize the comparator with a numeric value."""
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
    # Create a sample object with an internal value of 105
    comparator = NumberComparator(105)

    # Test cases
    assert comparator.is_greater_than(100) is True, "Should be greater than 100"
    assert comparator.is_greater_than(106) is False, "Should not be greater than 106"
    assert comparator.is_greater_than(-50) is True, "Should be greater than -50"

    # Demonstration with different inputs
    test_values = [99.5, 200, 'string']

    for val in test_values:
        try:
            result = comparator.is_greater_than(val)
            print(f"{comparator.value} > {val}: {result}")
        except TypeError:
            # Comparison with non-numeric types will raise an error internally if strict comparison is attempted by Python logic, 
            # but since the attribute holds a float/int, we just let natural behavior occur or handle type safety explicitly.
            print(f"Cannot compare {comparator.value} (type int) > {val} ({type(val).__name__})")

    print("\nAll tests executed successfully.")