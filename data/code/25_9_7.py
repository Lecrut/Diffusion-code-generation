class DataProcessor:
    def __init__(self, value):
        """Initialize instance attribute 'value'."""
        self.value = value
    
    def is_zero(self) -> bool:
        """Check if the instance attribute 'value' is equal to zero.
        
        Returns:
            True if self.value == 0, False otherwise.
        """
        return self.value == 0

if __name__ == '__main__':
    processor_1 = DataProcessor(5)
    processor_2 = DataProcessor(0)
    
    print(f"{processor_1.__class__.__name__} value is zero: {processor_1.is_zero()}")
    print(f"{processor_2.__class__.__name__} value is zero: {processor_2.is_zero()}")