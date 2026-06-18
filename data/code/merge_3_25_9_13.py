class DataProcessor:
    def __init__(self):
        self.counter = 0
    
    def is_zero(self, attribute_name="counter"):
        """Check if a specific instance attribute equals zero."""
        value = getattr(self, attribute_name)
        return value == 0

if __name__ == '__main__':
    processor = DataProcessor()
    
    # Test with initial default counter (which is 0)
    print(f"Is 'counter' equal to zero? {processor.is_zero('counter')}")
    
    # Simulate incrementing the attribute and re-check
    processor.counter = 100
    print(f"After setting to 100, is 'counter' equal to zero? {processor.is_zero('counter')}")