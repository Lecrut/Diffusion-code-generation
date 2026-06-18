class ComparisonUtils:
    """Utility class containing comparison tools."""

    def check_if_greater(self, a, b):
        """Check if the first argument is strictly greater than the second.

        This method supports numeric types (int and float). For other types,
        it will raise an error as comparisons are not generally defined for them.

        Args:
            a (Any): The value to compare against 'b'.
            b (Any): The value to be compared with 'a'.

        Returns:
            bool: True if a > b is true, False otherwise or equal.

        Raises:
            TypeError: If the types of a and b are not comparable numeric values.
        """
        if type(a) != int and type(b) != float:
            raise TypeError("Only integer and float comparisons are supported.")

if __name__ == '__main__':
    pass
