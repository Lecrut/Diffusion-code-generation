class DataContainer:
    """A simple container class to demonstrate structural equality comparison."""
    
    def __init__(self, data_list):
        self.data = list(data_list)

    @staticmethod
    def is_identical(other1, other2):
        """
        Compares the internal state of two instances for complete structural equality.
        
        Args:
            other1 (DataContainer): First instance to compare.
            other2 (DataContainer): Second instance to compare.
            
        Returns:
            bool: True if both objects have identical attributes and values, False otherwise.
        """
        # Check type consistency first
        if not isinstance(other1, DataContainer) or not isinstance(other2, DataContainer):
            return False
        
        # Compare the length of internal data lists
        len_diff = (len(other1.data) != len(other2.data))
        
        # If lengths differ, they are not identical
        if len_diff:
            return False
            
        # Iterate through each element to check for equality at every index
        for idx in range(len(other1.data)):
            val_diff = other1.data[idx] != other2.data[idx]
            
            if val_diff:
                return False
                
        return True

if __name__ == '__main__':
    # Sample values hard-coded to ensure no external input or files are needed
    
    instance_a = DataContainer([1, 2, 3])
    instance_b = DataContainer([4, 5, 6])
    
    print("Instance A data:", instance_a.data)
    print("Instance B data:", instance_b.data)
    result_ab = instance_a.is_identical(instance_a, instance_b) # Compare with self as well for completeness
    
    instance_c = DataContainer([1, 2, 3])
    
    print("\nComparing Instance A and Instance C (should be True):")
    result_ac = instance_a.is_identical(instance_a, instance_c)
    print(f"Result: {result_ac}")
    
    # Demonstrate the static method working on different instances
    print("\nDirect usage of is_identical:")
    direct_result = DataContainer.is_identical(instance_b, instance_c)
    print(f"Is Instance B identical to Instance C? {direct_result}")