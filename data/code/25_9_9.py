class DataProcessor:
    """A simple class to demonstrate checking instance attributes."""
    
    def __init__(self, value):
        self.value = value
    
    @staticmethod
    def check_zero(instance_attr_name, obj_instance):
        """
        Checks if a specific instance attribute of the provided object is equal to zero.

        Args:
            instance_attr_name (str): The name of the instance attribute to check.
            obj_instance: An instance of an object with that attribute.

        Returns:
            bool: True if the attribute equals 0, False otherwise.
        """
        return getattr(obj_instance, instance_attr_name) == 0

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or files
    
    processor = DataProcessor(10)
    
    print(f"Checking 'value' attribute of {processor}:")
    is_zero_value = check_zero('value', processor)
    print(is_zero_value)  # Expected: False

    zero_processor = DataProcessor(0)
    print(f"\nChecking 'value' attribute of {zero_processor}:")
    is_zero_val = check_zero('value', zero_processor)
    print(is_zero_val)  # Expected: True
    
    class Counter:
        def __init__(self, count):
            self.count = count
        
        @staticmethod
        def verify_count(obj_instance):
            return obj_instance.check_zero('count', obj_instance)

    counter_obj = Counter(5)
    print(f"\nChecking 'count' attribute of {counter_obj}:")
    is_zero_counter = check_zero('count', counter_obj)
    print(is_zero_counter)  # Expected: False
    
    zero_counter = Counter(0)
    print(f"Checking 'count' attribute of {zero_counter}:")
    is_zero_c = check_zero('count', zero_counter)
    print(is_zero_c)  # Expected: True