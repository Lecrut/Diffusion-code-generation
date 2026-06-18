class SampleClass:
    def __init__(self):
        self.value = 0
    
    def is_zero(self) -> bool:
        """Check if the instance attribute 'value' equals zero."""
        return self.value == 0

if __name__ == '__main__':
    obj1 = SampleClass()
    
    # Test with value equal to zero (default initialization)
    print(f"obj1.is_zero(): {obj1.is_zero()}")

    obj2 = SampleClass()
    obj2.value = 5
    
    # Modify an instance attribute and test again
    print(f"Modified obj2 is_zero: {obj2.is_zero()}")