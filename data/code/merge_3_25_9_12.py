class DataProcessor:
    def __init__(self, value):
        """Initialize the processor with a specific instance attribute."""
        self.current_value = value
    
    @property
    def is_zero(self):
        """Check if the current_instance_attribute equals zero.

        This method returns True if `current_value` is 0, otherwise False.
        It ensures that the comparison only involves this specific instance attribute.
        
        Returns:
            bool: True if self.current_value == 0, else False.
        """
        return self.current_value == 0

if __name__ == '__main__':
    # Sample block with hard-coded values to test functionality
    
    # Create instances with different initial values
    instance_a = DataProcessor(1)
    
    instance_b = DataProcessor(0)
    
    instance_c = DataProcessor(-5.0)  # Edge case: zero is numeric

    print(f"Instance A (value=1), is_zero? {instance_a.is_zero}")       # Expected False
    print(f"Instance B (value=0), is_zero? {instance_b.is_zero}")      # Expected True
    print(f"Instance C (value=-5.0), is_zero? {instance_c.is_zero}")  # Expected False
    
    # Verify return types and consistency
    assert isinstance(instance_a.is_zero, bool)
    assert instance_b.is_zero == True