class NumberChecker:
    def is_greater_than(self, other):
        """
        Checks if this instance's value is greater than another instance's value.
        
        Args:
            other (NumberChecker): The other number checker instance to compare against.
            
        Returns:
            bool: True if self.value > other.value, False otherwise.
        """
        return self.value > other.value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    obj1 = NumberChecker()
    obj2 = NumberChecker()

    # Set .value attributes directly since no constructor is provided in the task description.
    # We assume these are set externally or via a setter, but here we must ensure they exist.
    if not hasattr(obj1, 'value'):
        raise AttributeError("obj1 does not have a 'value' attribute.")
    
    obj1.value = 50

    if not hasattr(obj2, 'value'):
        raise AttributeError("obj2 does not have a 'value' attribute.")
        
    obj2.value = 30
    
    result = obj1.is_greater_than(obj2)
    
    print(f"Comparison: {obj1} vs {obj2}")
    print(f"{obj1.value > obj2.value}")