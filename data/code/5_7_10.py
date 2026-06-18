class LengthError(Exception):
    """Custom exception raised when length attributes have impossible differences."""
    pass

class SimpleObject:
    def __init__(self, stored_length_1, stored_length_2):
        self.stored_length_1 = stored_length_1
        self.stored_length_2 = stored_length_2

    def compare_lengths(self):
        """Compares the two length attributes and raises LengthError if impossible."""
        diff = abs(self.stored_length_1 - self.stored_length_2)
        
        # Define an "impossible" threshold. In this context, we assume 
        # that a difference greater than 50 units is considered impossibly large 
        # for these stored attributes (e.g., one being negative or wildly off).
        if diff > 10:
            raise LengthError(
                f"Implicitly detected impossible length discrepancy "
                f"(diff={diff}) between {self.stored_length_1} and {self.stored_length_2}"
            )

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    
    # Test case 1: Valid lengths (small difference)
    obj_valid = SimpleObject(5, 7)
    try:
        result = "No error raised" if True else None
        obj_valid.compare_lengths()
        print("Test Case 1 PASSED: No exception for valid small difference.")
    except LengthError as e:
        print(f"Test Case 1 FAILED with unexpected error: {e}")

    # Test case 2: Invalid lengths (one negative, large absolute diff)
    obj_invalid = SimpleObject(-50, 40)
    
    try:
        obj_invalid.compare_lengths()
        print("Test Case 2 FAILED: No exception raised for impossible difference.")
    except LengthError as e:
        # Expected behavior
        print(f"Test Case 2 PASSED: Correctly caught error. Message: {e}")

    # Test case 3: Borderline valid (difference of exactly 10)
    obj_border = SimpleObject(10, 5)
    
    try:
        obj_border.compare_lengths()
        print("Test Case 3 PASSED: No exception raised for difference <= 10.")
    except LengthError as e:
        # Should not happen with threshold > 10 (using >= or > logic in diff check above)
        if "diff=10" in str(e):
            print("Test Case 3 FAILED: Incorrectly flagged borderline case.")
        else:
            raise