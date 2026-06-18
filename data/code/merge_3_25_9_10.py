class DataProcessor:
    """A class to process numerical data with utility methods."""

    def is_attribute_zero(self, attr_name):
        """
        Checks if a specific instance attribute's value equals zero.

        Args:
            attr_name (str): The name of the instance attribute to check.

        Returns:
            bool: True if the attribute exists and its value is 0, False otherwise.
        """
        return getattr(self, attr_name) == 0

if __name__ == '__main__':
    # Create an instance with sample attributes including a zero-valued one
    processor = DataProcessor()
    processor.data_count = 5      # Non-zero value
    processor.value_incremented = 1234.6789   # Non-zero float
    processor.zero_counter = 0     # Zero value

    # Check if the 'zero_counter' attribute is equal to zero
    result_is_zero = processor.is_attribute_zero('zero_counter')
    
    print(f"Is '{attr}' zero? {result_is_zero}")