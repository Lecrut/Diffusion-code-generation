class LengthError(Exception):
    """Custom exception raised when length attributes have impossibly different values."""
    pass

class SimpleObject:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def validate_dimensions(self):
        """Compares stored length attributes and raises LengthError if invalid."""
        # Check for negative lengths which are physically impossible in this context
        if self.width < 0 or self.height < 0:
            raise LengthError(f"Impossibly different/negative dimensions found: width={self.width}, height={self.height}")

    def __repr__(self):
        return f"SimpleObject(width={self.width}, height={self.height})"

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input or files
    
    # Test case 1: Valid positive dimensions (should pass)
    obj_valid = SimpleObject(5, 3)
    
    try:
        print("Testing valid object...")
        obj_valid.validate_dimensions()
        print(f"Validation passed for {obj_valid}")
    except LengthError as e:
        print(f"Unexpected error in test case 1: {e}")

    # Test case 2: Negative width (should raise exception)
    obj_invalid = SimpleObject(-5, 3)
    
    try:
        print("Testing invalid object with negative width...")
        obj_invalid.validate_dimensions()
        print(f"Validation unexpectedly passed for {obj_invalid}")
    except LengthError as e:
        print(f"Expected error caught in test case 2: {e}")

    # Test case 3: Negative height (should raise exception)
    obj_invalid_height = SimpleObject(5, -10)
    
    try:
        print("Testing invalid object with negative height...")
        obj_invalid_height.validate_dimensions()
        print(f"Validation unexpectedly passed for {obj_invalid_height}")
    except LengthError as e:
        print(f"Expected error caught in test case 3: {e}")

    # Test case 4: Both zero (valid edge case)
    obj_zero = SimpleObject(0, 0)
    
    try:
        print("Testing object with zero dimensions...")
        obj_zero.validate_dimensions()
        print(f"Validation passed for {obj_zero}")
    except LengthError as e:
        print(f"Unexpected error in test case 4: {e}")

    # Test case 5: Very large difference (valid mathematically, but let's ensure logic holds)
    obj_large_diff = SimpleObject(1000000, -1)
    
    try:
        print("Testing object with huge positive and negative diff...")
        obj_large_diff.validate_dimensions()
        print(f"Validation unexpectedly passed for {obj_large_diff}")
    except LengthError as e:
        print(f"Expected error caught in test case 5: {e}")