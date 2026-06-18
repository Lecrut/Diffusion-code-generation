class DataProcessor:
    def __init__(self):
        self.value = 10
    
    @property
    def is_zero(self) -> bool:
        """Check if the instance attribute 'value' is equal to zero."""
        return self.value == 0

if __name__ == '__main__':
    processor = DataProcessor()

    # Test case with non-zero value (default initialization)
    print(f"Default value ({processor.value}): {processor.is_zero}")

    # Simulate updating the attribute to zero for testing
    processor.value = 0
    print(f"After setting to 0: {processor.value} -> Is Zero? {processor.is_zero}")