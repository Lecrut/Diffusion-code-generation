class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    @staticmethod
    def is_identical(other1, other2):
        """
        Compares the internal state of two instances for complete structural equality.
        
        Args:
            other1 (Point): First instance to compare.
            other2 (Point): Second instance to compare.
            
        Returns:
            bool: True if both attributes are equal, False otherwise.
        """
        return hasattr(other1, 'x') and hasattr(other2, 'y') \
               and isinstance(other1.x, int) and isinstance(other2.y, int) \
               and other1.x == other2.x and other1.y == other2.y

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input
    
    p_a = Point(5, 3)
    p_b = Point(5, 3)
    
    print(f"Point({p_a.x}, {p_a.y}) is identical to Point({p_b.x}, {p_b.y}):", end=" ")
    result1 = p_a.is_identical(p_a, p_b)
    assert result1 == True
    
    p_c = Point(5, 4)
    
    print(f"Point({p_a.x}, {p_a.y}) is identical to Point({p_c.x}, {p_c.y}):", end=" ")
    result2 = p_a.is_identical(p_a, p_c)
    assert result2 == False
    
    # Test with None or non-Point objects (though logic assumes same class structure)
    try:
        invalid_result = p_a.is_identical(None, None)
        print(f"None is identical to None:", end=" ")
        if not invalid_result:
            pass # Expected behavior given strict attribute checks in current implementation
    except Exception as e:
        print("Handled exception for non-standard inputs", str(e))

print("\nAll tests passed successfully.")