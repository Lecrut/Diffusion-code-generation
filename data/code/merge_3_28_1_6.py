class ComparisonUtils:
    """A utility class containing comparison methods."""

    @staticmethod
    def check_if_greater(value1, value2):
        """
        Compares two values of any comparable type and returns a boolean indicating
        whether the first argument is strictly greater than the second.

        Args:
            value1 (Comparable): The first value to compare.
            value2 (Comparable): The second value to compare.

        Returns:
            bool: True if value1 > value2, False otherwise.

        Raises:
            TypeError: If either argument is not comparable with the other.
        """
        try:
            return value1 > value2
        except TypeError:
            raise TypeError(f"Cannot compare {type(value1).__name__} and {type(value2).__name__}")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    # Test with integers
    result_int = ComparisonUtils.check_if_greater(5, 3)
    print(f"Integers: 5 > 3 is {result_int}")

    # Test with floats
    result_float = ComparisonUtils.check_if_greater(2.718, 2.714)
    print(f"Floats: 2.718 > 2.714 is {result_float}")

    # Test where first value is smaller
    result_less = ComparisonUtils.check_if_greater(3, 5)
    print(f"Integers (smaller): 3 > 5 is {result_less}")

    # Test with strings
    result_str = ComparisonUtils.check_if_greater("zebra", "apple")
    print(f"strings: 'zebra' > 'apple' is {result_str}")

    # Demonstrate error handling attempt implicitly by calling valid code only, 
    # but the method definition handles TypeError if invalid types were passed.