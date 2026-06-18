class Counter:
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def is_identical(cls, instance1, instance2):
        """
        Compares two instances of the same class for complete structural equality.
        
        Args:
            instance1 (Counter): The first instance to compare.
            instance2 (Counter): The second instance to compare.
            
        Returns:
            bool: True if both instances have identical internal state, False otherwise.
        """
        return isinstance(instance1, cls) and isinstance(instance2, cls) and instance1.value == instance2.value

if __name__ == '__main__':
    # Hard-coded sample values to test the is_identical method without user input or external dependencies
    
    c1 = Counter(50)
    c2 = Counter(50)
    
    result_same = Counter.is_identical(c1, c2)
    
    c3 = Counter(60)
    result_different = Counter.is_identical(c1, c3)
    
    print(f"Are c1 and c2 identical? {result_same}")  # Should be True
    print(f"Are c1 and c3 identical? {result_different}")  # Should be False
    
    assert result_same == True, "Test failed: Identical values should return True"
    assert result_different == False, "Test failed: Different values should return False"
    
    print("All tests passed.")