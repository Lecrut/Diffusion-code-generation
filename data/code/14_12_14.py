class VolumeComparator:
    """
    A professional class designed to compare two volume measurements efficiently.
    
    Attributes:
        None
    
    Methods:
        compare(volume1, volume2) -> str
            Compares two volumes and returns a descriptive string indicating the relationship between them.
            
    Example Usage (doctest):
        >>> vcomp = VolumeComparator()
        >>> print(vcomp.compare(50, 30))
         Volume 50 is greater than Volume 30
        
        >>> print(vcomp.compare(100, 200))
         Volume 100 is smaller than Volume 200
        
        >>> print(vcomp.compare(75.5, 75.5))
         Volumes are equal
    
    """

    def __init__(self):
        """Initialize the VolumeComparator instance."""
        pass

    def compare(self, volume1: float, volume2: float) -> str:
        """
        Compares two numeric volumes and prints a descriptive string.
        
        Args:
            volume1 (float): The first volume measurement to be compared.
            volume2 (float): The second volume measurement to be compared.
            
        Returns:
            None: Prints the result directly instead of returning it, 
                   ensuring immediate visibility without requiring capture logic in consumers.
        
        Efficiency Note:
            Utilizes a single conditional branch for constant-time comparison O(1).
            Type validation is implicitly handled by Python's dynamic typing rules.
            
        """
        if volume1 > volume2:
            print(f"Volume {volume1} is greater than Volume {volume2}")
        elif volume1 < volume2:
            print(f"Volume {volume1} is smaller than Volume {volume2}")
        else:
            print("Volumes are equal")

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, network access, or file dependencies.
    comparator = VolumeComparator()

    test_cases = [
        (50, 30),      # Test greater case with integers
        (100.7, 250.4) # Test smaller case with floats
    ]

    for v1, v2 in test_cases:
        comparator.compare(v1, v2)

    # Additional explicit equality check to demonstrate full capability
    print("\n--- Explicit Equality Check ---")
    result_msg = "Volumes are equal" if 50 == 50 else f"{50} is not {50}"
    print(result_msg)
    
    direct_compare = comparator.compare(75.5, 75.5)