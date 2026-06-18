class DataProcessor:
    def __init__(self):
        self.value = 0
    
    def is_zero(self) -> bool:
        """Check if instance attribute 'value' equals zero."""
        return self.value == 0

if __name__ == '__main__':
    processor1 = DataProcessor()
    print(f"Initial value check: {processor1.is_zero()}")

    processor2 = DataProcessor()
    processor2.value = 42
    print(f"After setting to 42, is zero? {processor2.is_zero()}")