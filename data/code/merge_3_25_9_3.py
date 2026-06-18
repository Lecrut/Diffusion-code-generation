class DataProcessor:
    """A simple class demonstrating instance attribute checking."""

    def __init__(self, value):
        self.value = value

    @staticmethod
    def is_zero(instance_attr_name, obj=None):
        """
        Check if a specific instance attribute equals zero.

        Args:
            instance_attr_name (str): Name of the instance attribute to check.
            obj (object, optional): The object whose attributes are being checked. Defaults to self.

        Returns:
            bool: True if the attribute is 0, False otherwise.
        """
        return getattr(obj, instance_attr_name) == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    processor = DataProcessor(42)

    print(f"Is 'value' zero? {processor.is_zero('value', obj=processor)}")

    # Create another instance with a different value to verify behavior
    processor_two = DataProcessor(0)
    print(f"Is 'value' zero for second instance? {processor_two.is_zero('value', obj=processor_two)}")