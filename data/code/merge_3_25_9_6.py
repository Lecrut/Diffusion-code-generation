class DataProcessor:
    """A class that provides utility methods to check instance attributes."""

    def is_zero(self, attribute_name):
        """
        Check if a specific instance attribute equals zero.

        Args:
            attribute_name (str): The name of the attribute to inspect as a string.

        Returns:
            bool: True if the attribute exists and its value is 0, False otherwise.
        """
        return getattr(self, attribute_name) == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    processor = DataProcessor()

    # Set up some instance attributes including one that is zero and others that are not.
    processor.count_items = 5
    processor.balance = 0
    processor.status = "active"

    # Test the method with different attribute names.
    print("Is count_items equal to zero?", processor.is_zero('count_items'))
    print("Is balance equal to zero?", processor.is_zero('balance'))
    print("Is status equal to zero?", processor.is_zero('status'))