class LengthError(Exception):
    """Custom exception raised when length attributes have impossible differences."""
    pass

class SimpleObject:
    def __init__(self, stored_length_1: int, stored_length_2: int) -> None:
        self.stored_length_1 = stored_length_1
        self.stored_length_2 = stored_length_2

    def validate_lengths(self) -> bool:
        """
        Compares the two stored length attributes.
        
        Raises a LengthError if either value is negative 
        or if their absolute difference exceeds 50 units,
        considered 'impossibly different' for this context.
        
        Returns True otherwise.
        """
        # Check for impossible individual values (negative lengths)
        if self.stored_length_1 < 0:
            raise LengthError(f"Length attribute 1 is negative ({self.stored_length_1})")
        if self.stored_length_2 < 0:
            raise LengthError(f"Length attribute 2 is negative ({self.stored_length_2})")

        # Check for impossibly different values (difference > 50)
        diff = abs(self.stored_length_1 - self.stored_length_2)
        if diff > 50:
            raise LengthError(f"Lengths are too different by {diff} units.")

        return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    # Test Case 1: Valid lengths with small difference
    obj_valid = SimpleObject(10, 25)
    try:
        result = obj_valid.validate_lengths()
        print(f"Test 1 (Valid): Passed. Result: {result}")
    except LengthError as e:
        print(f"Test 1 Failed with error: {e}")

    # Test Case 2: One negative length
    obj_negative_1 = SimpleObject(-5, 10)
    try:
        result = obj_negative_1.validate_lengths()
        print("Test 2 (Negative Length): Should have raised an exception")
    except LengthError as e:
        print(f"Test 2 Passed. Caught expected error: {e}")

    # Test Case 3: Impossibly different lengths (>50 difference)
    obj_diff = SimpleObject(1, 60)
    try:
        result = obj_diff.validate_lengths()
        print("Test 3 (Too Different): Should have raised an exception")
    except LengthError as e:
        print(f"Test 3 Passed. Caught expected error: {e}")

    # Test Case 4: Both zero and equal difference of 0
    obj_equal = SimpleObject(0, 0)
    try:
        result = obj_equal.validate_lengths()
        print("Test 4 (Equal): Passed. Result:", result)
    except LengthError as e:
        print(f"Test 4 Failed with error: {e}")

    # Test Case 5: Edge case difference exactly at limit (50 is allowed, >50 not)
    obj_edge = SimpleObject(10, 60)
    try:
        result = obj_edge.validate_lengths()
        print("Test 5 (Edge Difference=50): Passed. Result:", result)
    except LengthError as e:
        print(f"Test 5 Failed with error: {e}")

    # Test Case 6: Edge case difference just over limit (51 is not allowed)
    obj_over_edge = SimpleObject(10, 61)
    try:
        result = obj_over_edge.validate_lengths()
        print("Test 6 (Over Edge Difference=51): Should have raised an exception")
    except LengthError as e:
        print(f"Test 6 Passed. Caught expected error: {e}")