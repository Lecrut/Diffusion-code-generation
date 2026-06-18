class DataProcessor:
    def __init__(self):
        self.value = 10
    
    @property
    def is_zero(self) -> bool:
        """Check if the instance attribute 'value' equals zero."""
        return self.value == 0

if __name__ == '__main__':
    processor = DataProcessor()

    # Test with initial value (non-zero)
    print(f"Initial value ({processor.value}): {not processor.is_zero}")

    # Simulate setting the attribute to zero and checking again
    processor.value = 0
    print(f"After setting to 0: {processor.is_zero}")

    # Reset for another test case demonstration
    processor.value = 5
    print(f"Value set to 5: {not processor.is_zero}")