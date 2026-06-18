class LengthError(Exception):
    """Custom exception raised when length attributes have impossible differences."""
    pass

class SimpleObject:
    def __init__(self, stored_length_a=10, stored_length_b=20):
        self.stored_length_a = stored_length_a
        self.stored_length_b = stored_length_b

    def validate_lengths(self):
        """Compares the two length attributes and raises LengthError if impossible."""
        diff = abs(self.stored_length_a - self.stored_length_b)
        
        # Check for impossibly different lengths (e.g., one negative, or extreme disparity > 1000)
        if self.stored_length_a < 0 or self.stored_length_b < 0:
            raise LengthError(f"Lengths cannot be negative. Found {self.stored_length_a} and {self.stored_length_b}.")
        
        # Consider a difference greater than 1000 as "impossibly different" for this context
        if diff > 1000:
            raise LengthError(
                f"The lengths are impossibly different. Difference of {diff}, "
                f"{self.stored_length_a} vs {self.stored_length_b}. They should be closer."
            )

if __name__ == '__main__':
    # Hard-coded sample values demonstrating the validation logic
    
    print("Test Case 1: Valid lengths with small difference")
    obj_valid = SimpleObject(stored_length_a=50, stored_length_b=60)
    try:
        obj_valid.validate_lengths()
        print("Validation passed.")
    except LengthError as e:
        print(f"Unexpected error: {e}")

    print("\nTest Case 2: One negative length")
    obj_negative = SimpleObject(stored_length_a=-10, stored_length_b=5)
    try:
        obj_negative.validate_lengths()
        print("Validation passed.")
    except LengthError as e:
        print(f"Caught expected error: {e}")

    print("\nTest Case 3: Impossibly large difference")
    obj_large_diff = SimpleObject(stored_length_a=0, stored_length_b=2000)
    try:
        obj_large_diff.validate_lengths()
        print("Validation passed.")
    except LengthError as e:
        print(f"Caught expected error: {e}")

    print("\nTest Case 4: Both zero (valid edge case)")
    obj_zero = SimpleObject(stored_length_a=0, stored_length_b=0)
    try:
        obj_zero.validate_lengths()
        print("Validation passed.")
    except LengthError as e:
        print(f"Unexpected error: {e}")

    print("\nAll tests completed successfully without external input or files.")