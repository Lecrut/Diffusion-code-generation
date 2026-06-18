class DataContainer:
    """A simple container class to hold various data types."""
    
    def __init__(self, value1=0, value2=None):
        self.value1 = value1
        self.value2 = value2
    
    @classmethod
    def is_identical(cls, instance_a, instance_b):
        """
        Compares the internal state of two instances for complete structural equality.
        
        Args:
            instance_a (DataContainer): The first instance to compare.
            instance_b (DataContainer): The second instance to compare.
            
        Returns:
            bool: True if both objects have identical attributes with equal values, False otherwise.
        """
        # Check for basic type mismatch immediately
        if not isinstance(instance_a, cls) or not isinstance(instance_b, cls):
            return False
            
        try:
            # Compare all public instance attributes directly
            attrs = [attr for attr in dir(instance_a) 
                     if not attr.startswith('_') and hasattr(cls, attr)]
            
            # Ensure both have the same set of comparable attributes
            missing_in_b = set(attrs) - {a for a in dir(instance_b) if not a.startswith('_')}
            extra_in_a = {a for a in attrs if a not in [b for b in dir(instance_b) if not b.startswith('_')]}
            
            # If attribute sets differ, they are not identical structurally based on defined attributes
            if missing_in_b or extra_in_a:
                return False
            
            # Compare values of all public attributes
            for attr_name in attrs:
                val_a = getattr(instance_a, attr_name)
                val_b = getattr(instance_b, attr_name)
                
                # Use deep equality check (== handles lists, dicts, numbers correctly)
                if val_a != val_b:
                    return False
            
            return True
        except AttributeError:
            # Fallback for any unexpected attribute access errors during comparison
            return False

if __name__ == '__main__':
    # Hard-coded sample values to test the is_identical method
    
    instance_one = DataContainer(10, "Hello")
    instance_two = DataContainer(10, "Hello")
    
    result_same = DataContainer.is_identical(instance_one, instance_two)
    
    different_instance = DataContainer(20, "World")
    result_different = DataContainer.is_identical(instance_one, different_instance)
    
    print(f"Identical instances: {result_same}")  # Should be True
    print(f"Different instances: {result_different}")  # Should be False
    
    assert result_same == True
    assert result_different == False