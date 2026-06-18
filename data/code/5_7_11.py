class LengthError(Exception):
    """Custom exception raised when length attributes have impossibly different values."""
    pass

def validate_lengths(obj1, obj2):
    """
    Compares two stored length attributes from objects and raises a custom exception
    if the lengths are impossibly different (e.g., one is negative).

    Args:
        obj1: An object with an attribute 'length'.
        obj2: Another object with an attribute 'length'.

    Raises:
        LengthError: If either length is negative or they differ by more than 5 units.
    """
    len1 = getattr(obj1, 'length', None)
    len2 = getattr(obj2, 'length', None)

    if len1 is not None and (len1 < 0):
        raise LengthError(f"Impossibly different lengths: {obj1} has a negative length ({len1}).")
    
    if len2 is not None and (len2 < 0):
        raise LengthError(f"Impossibly different lengths: {obj2} has a negative length ({len2}).")

    # Check for significant difference in positive values
    if len1 >= 0 and len2 >= 0:
        diff = abs(len1 - len2)
        if diff > 5:
            raise LengthError(f"Impossibly different lengths: {obj1} has length {len1}, {obj2} has length {len2}. Difference is too large.")

class SimpleObject:
    """A simple container for a single numeric attribute."""

    def __init__(self, name, value):
        self.name = name
        self.length = value

if __name__ == '__main__':
    # Hard-coded sample values to test the validation logic without user input.
    
    obj_a = SimpleObject("Item A", 10)
    obj_b = SimpleObject("Item B", -5)

    try:
        validate_lengths(obj_a, obj_b)
        print("Validation passed.")
    except LengthError as e:
        print(f"Length validation failed: {e}")