class DataProcessor:
    def __init__(self):
        self.value = 10
    
    @staticmethod
    def check_zero(instance, attribute_name):
        """
        Checks if a specific instance attribute is equal to zero.
        
        Args:
            instance (object): The object whose attributes are being checked.
            attribute_name (str): The name of the attribute to inspect.
            
        Returns:
            bool: True if the attribute equals 0, False otherwise.
        """
        return getattr(instance, attribute_name) == 0

if __name__ == '__main__':
    processor = DataProcessor()
    
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test case 1: Attribute is zero
    if DataProcessor.check_zero(processor, 'value'):
        print("Value is zero.")
    else:
        print(f"Value ({processor.value}) is not zero.")

    # Simulate changing the value to test again (optional demonstration)
    processor.value = 0
    
    if DataProcessor.check_zero(processor, 'value'):
        print("Updated Value is now zero.")