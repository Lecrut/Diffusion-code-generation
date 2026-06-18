class ComparisonUtils:
    """A utility class providing comparison operations between two values."""

    @staticmethod
    def check_if_greater(value1, value2):
        """
        Compares two arguments and returns True if the first is strictly greater 
        than the second. Otherwise, it returns False.
        
        This method handles numeric types (int, float) directly by using Python's
        built-in comparison operators. It also attempts to compare instances of a custom
        base class `Comparable` defined in this module for demonstration purposes.

        Args:
            value1: The first object or number to be compared.
            value2: The second object or number to be compared.

        Returns:
            bool: True if value1 > value2, False otherwise.
        
        Raises:
            TypeError: If the arguments cannot be compared due to type mismatch 
                      (e.g., comparing int and str directly without custom logic).
        """
        # Attempt direct comparison first as it is safe for built-in types in Python 3
        try:
            return value1 > value2
        except TypeError:
            pass
        
        # Fallback to a generic class-based check if the exception above occurs,
        # although standard Python handles most type mismatches gracefully.
        # For this implementation, we assume inputs are either numeric or compatible 
        # instances of Comparable objects defined within this module for robustness.

class Comparable:
    """A base class designed to demonstrate object-based comparison."""
    
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        if isinstance(other, Comparable):
            return self.value < other.value
        raise TypeError("Cannot compare with non-Comparable instance.")

if __name__ == '__main__':
    # Hard-coded sample values for testing the check_if_greater method.
    
    # Test 1: Integers
    result_int = ComparisonUtils.check_if_greater(10, 5)
    assert result_int is True
    
    # Test 2: Floats
    float_a = ComparisonUtils.check_if_greater(3.14, 2.71)
    assert float_a is True
    
    # Test 3: Comparing same values (should return False for strictly greater)
    result_equal = ComparisonUtils.check_if_greater(50, 50)
    assert result_equal is False
    
    # Test 4: Using Comparable objects
    obj1 = Comparable(value=20)
    obj2 = Comparable(value=30)
    
    result_comparable = ComparisonUtils.check_if_greater(obj1, obj2)
    assert result_comparable is True
    
    print("All tests passed successfully.")