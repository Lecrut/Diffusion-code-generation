class DataProcessor:
    def __init__(self):
        self.value = 0
    
    @staticmethod
    def is_zero(instance, attribute_name="value"):
        """
        Checks if a specific instance attribute equals zero.
        
        Args:
            instance (object): The object to inspect.
            attribute_name (str): Name of the attribute to check. Defaults to 'value'.
            
        Returns:
            bool: True if the attribute is 0, False otherwise.
        """
        return getattr(instance, attribute_name) == 0

if __name__ == '__main__':
    processor = DataProcessor()
    
    # Hard-coded sample values
    test_cases = [
        ("zero_value", 5),      # Expected: True (attribute is zero) -> False in this context as value=5, but let's adjust logic for clarity below. 
                                # Actually the task says "checks if ... equal to zero". So if attribute IS zero, return True.
    ]

    # Let's create instances with specific values for testing
    instance_one = DataProcessor()
    instance_two = DataProcessor()
    
    # Manually set attributes for demonstration without relying on __init__ default being the only source of truth
    instance_one.value = 0      # Should be True
    instance_two.value = 42     # Should be False

    print(f"Is {instance_one.__class__.__name__} attribute 'value' zero? {DataProcessor.is_zero(instance_one, 'value')}")
    print(f"Is {instance_two.__class__.__name__} attribute 'value' zero? {DataProcessor.is_zero(instance_two, 'value')}")

    # Test with a different instance type to ensure it works on any object
    class Counter:
        def __init__(self):
            self.count = 0
    
    counter_obj = Counter()
    counter_obj.count = 100
    
    print(f"Is {Counter.__name__} attribute 'count' zero? {DataProcessor.is_zero(counter_obj, 'count')}")