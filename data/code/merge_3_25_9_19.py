class DataProcessor:
    """A simple class demonstrating a method to check if an instance attribute is zero."""

    def __init__(self, value):
        self.value = value

    def is_zero(self) -> bool:
        """Check if the instance attribute 'value' equals zero.

        Returns:
            bool: True if self.value is 0, False otherwise.
        """
        return self.value == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files.
    instance_positive = DataProcessor(15)
    instance_negative = DataProcessor(-3)
    instance_zero = DataProcessor(0)

    print(f"Is {instance_positive.value} zero? {instance_positive.is_zero()}")  # False
    print(f"Is {instance_negative.value} zero? {instance_negative.is_zero()}")  # False
    print(f"Is {instance_zero.value} zero? {instance_zero.is_zero()}")        # True