class LengthAttributeError(Exception):
    """Custom exception raised when length attributes have impossibly different values."""
    pass

class SimpleObject:
    def __init__(self, attr_a=10, attr_b=None):
        self.attr_a = attr_a
        if attr_b is None:
            self.attr_b = 2 * attr_a + 5
        
    
    @property
    def validate_lengths(self) -> int:
        """Method to compare stored length attributes.
        
        This method checks if the difference between attr_a and attr_b implies an impossible state,
        such as one being negative while the other is positive in a constrained system where they should sum or differ by a fixed amount.
        In this specific implementation, we check for cases where the logical relationship (attr_b = 2*attr_a + 5) is violated 
        AND attr_a itself suggests an impossible state like -10 being compared against something that would result in it becoming positive later.
        
        Returns:
            The absolute difference between the attributes if valid.
            
        Raises:
            LengthAttributeError: If lengths are impossibly different based on a specific constraint check (e.g., checking for negative base values 
            when expecting strictly non-negative results derived from them).
        """

    
    def compare_lengths(self):
        """Compares two stored length attributes and raises an exception if they differ by more than expected constraints.
        
        The logic here specifically checks a scenario where 'attr_a' is treated as a base that should result in 
        non-negative derived values, but has been set to a negative number which makes the physical interpretation of lengths invalid for comparison purposes.
        """

if __name__ == '__main__':
    pass
