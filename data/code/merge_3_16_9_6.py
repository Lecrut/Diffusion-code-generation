class PositivityChecker:
    """Utility class containing static methods to determine if a value is positive."""

    @staticmethod
    def is_positive(value):
        """Check if a number is strictly greater than zero.
        
        Args:
            value (int | float): The numerical value to check.
            
        Returns:
            bool: True if the value is greater than 0, False otherwise.
        """
        return isinstance(value, (int, float)) and value > 0

if __name__ == '__main__':
    pass
