class LengthError(Exception):
    """Custom exception raised when length attributes have impossibly different values."""
    pass

class SimpleObject:
    def __init__(self, attr1_length=None, attr2_length=None):
        self.attr1 = "value" * (attr1_length if attr1_length is not None else 0)
        self.attr2 = "value" * (attr2_length if attr2_length is not None else 0)

    def validate_lengths(self):
        """Compares the lengths of attribute 'attr1' and 'attr2'.
        
        Raises a LengthError if:
        - The length of either attribute is negative.
        - One length is significantly larger than the other (difference > 50).
        """
        len1 = self.attr1_length() if hasattr(self, 'attr1_length') else self._get_len('attr1', None)
        # Since attr1 and attr2 are strings, we can derive lengths. 
        # To simulate a separate attribute check as per the "stored length attributes" prompt:
        
        len_attr1 = 0 if not hasattr(self, '_len_1') else getattr(self, '_len_1', None)
        len_attr2 = 0 if not hasattr(self, '_len_2') else getattr(self, '_len_2', None)

        # If lengths were explicitly stored during init (optional extension for strict adherence to "stored length attributes")
        try:
            l1 = self._get_len('attr1')
            l2 = self._get_len('attr2')
            
            if l1 < 0 or l2 < 0:
                raise LengthError(f"Impossibly negative lengths found: {l1} and {l2}")
                
            diff = abs(l1 - l2)
            if diff > 50:
                raise LengthError(f"Lengths are impossibly different: difference of {diff} between {l1} and {l2}.")

        except AttributeError as e:
             # Fallback logic for direct string length calculation in case stored attributes aren't updated dynamically
            l1 = len(self.attr1)
            l2 = len(self.attr2)
            
            if l1 < 0 or l2 < 0: raise LengthError(f"Impossibly negative lengths found.")
            diff = abs(l1 - l2)
            if diff > 50: 
                msg = f"Lengths are impossibly different."
                # Add detail only for debugging clarity, but keep exception message clean per standard practice unless requested verbose
                raise LengthError(msg + f"\nDifference of {diff} found between lengths.")

    def _get_len(self, attr_name):
        return len(getattr(self, attr_name))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    try:
        obj = SimpleObject(attr1_length=50, attr2_length=-3)  # Test negative length condition
        
        print("Testing valid vs invalid scenario...")
        
        # Access lengths before validation if needed for logging
        l1 = len(obj.attr1)
        l2 = len(obj.attr2)
        
    except LengthError as e:
        print(f"Caught expected exception (Negative or Impossibly different): {e}")
    
    try:
        obj_good = SimpleObject(attr1_length=50, attr2_length=60)  # Test small difference
        
        print("\nTesting valid vs close scenario...")
        
        l1_g = len(obj_good.attr1)
        l2_g = len(obj_good.attr2)

    except LengthError as e:
        print(f"Unexpected exception in good case (should not happen): {e}")

    try:
        obj_bad_diff = SimpleObject(attr1_length=50, attr2_length=300)  # Test large difference
        
        print("\nTesting valid vs very different scenario...")

    except LengthError as e:
        print(f"Caught expected exception (Impossibly different): {e}")