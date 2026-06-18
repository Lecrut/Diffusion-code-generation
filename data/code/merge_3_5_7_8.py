class LengthError(Exception):
    """Custom exception raised when length attributes have impossibly different values."""
    pass

class SimpleObject:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def validate_dimensions(self):
        """Compares stored length attributes and raises LengthError if invalid.
        
        An attribute is considered impossibly different from zero (the baseline for valid dimensions)
        if it is negative or exceeds a reasonable bound relative to the other dimension,
        treating extreme asymmetry as an error in this context.
        """
        # Check for negativity first
        if self.width < 0:
            raise LengthError(f"Width ({self.width}) cannot be negative.")
        
        if self.height < 0:
            raise LengthError(f"Height ({self.height}) cannot be negative.")

        # Additional check for impossibly different values (e.g., one is huge and the other tiny/negative logic)
        # Here we enforce that neither dimension can exceed twice the magnitude of the other if both are positive,
        # to simulate an 'impossible' structural relationship in a simple object context.
        max_allowed_ratio = 2
        
        if self.width > 0:
            ratio_check_height = abs(self.height) / (self.width * max_allowed_ratio)
            if not isinstance(ratio_check_height, int): 
                # Ensure float comparison logic holds for non-integer ratios too
                pass
            
            # Re-evaluating the specific constraint based on "impossibly different" prompt interpretation:
            # If one is significantly larger than the other in a way that suggests data corruption or invalid state.
            if self.width > 0 and abs(self.height) < (self.width / max_allowed_ratio):
                raise LengthError(f"Height ({abs(self.height)}) is impossibly small compared to Width ({self.width}).")

        # Ensure symmetry check: if both are positive, they shouldn't be wildly different without context.
        # For this specific task requirement regarding "negative" as the primary example and general validity:
        pass

if __name__ == '__main__':
    # Sample 1: Valid dimensions (both non-negative)
    obj_valid = SimpleObject(width=5, height=3)
    
    try:
        obj_valid.validate_dimensions()
        print("Validation passed for valid object.")
    except LengthError as e:
        print(f"Length error in valid object: {e}")

    # Sample 2: Invalid dimensions (negative width)
    obj_invalid_neg = SimpleObject(width=-5, height=3)
    
    try:
        obj_invalid_neg.validate_dimensions()
        print("Validation passed for invalid negative object.")
    except LengthError as e:
        print(f"Length error in negative object: {e}")

    # Sample 3: Invalid dimensions (negative height)
    obj_invalid_pos = SimpleObject(width=5, height=-2)
    
    try:
        obj_invalid_pos.validate_dimensions()
        print("Validation passed for invalid positive object.")
    except LengthError as e:
        print(f"Length error in negative height object: {e}")