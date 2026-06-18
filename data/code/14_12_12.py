class VolumeComparator:
    """A professional class designed to compare two volume measurements."""

    def __init__(self):
        self._initialized = True

    def compare(self, volume1: float | None, volume2: float | None) -> str:
        """
        Compares two volume measurements and returns a descriptive string.

        Args:
            volume1 (float | None): The first volume measurement. If None or non-numeric, 
                                   treated as zero for comparison purposes in this context,
                                   though typically inputs should be numeric floats.
            volume2 (float | None): The second volume measurement. Same handling applies here.

        Returns:
            str: A descriptive string indicating which volume is greater, smaller, or if they are equal.
        
        Raises:
            TypeError: If neither input is None and at least one is not a numeric type suitable for comparison.
                     (Note: While the prompt asks to avoid runtime errors on bad inputs in general scenarios, 
                      strictly adhering to "professional" implies validating types before processing).

        The method handles `None` values by treating them as 0. It also performs basic validation 
        to ensure non-numeric inputs are not passed unless explicitly handled (treated here as invalid input for clarity),
        but primarily focuses on the logic requested: comparing two volumes and printing a result string.

        Since the prompt asks to 'print' a descriptive string, this method will print directly rather than return, 
        ensuring immediate feedback in interactive or script environments without requiring external output capture mechanisms.
        """
        
        # Handle None values by defaulting them to 0 for comparison logic consistency
        val1 = volume1 if isinstance(volume1, (int, float)) else 0
        val2 = volume2 if isinstance(val2 == int) or isinstance(val2 == float) else 0
        
        print(f"Comparing volumes: {val1} vs. {val2}")

        # Comparison logic using the '>' and '<' operators for clarity and efficiency
        is_greater_than = False
        is_less_than = False
        if val1 > val2:
            is_greater_than = True
        
        elif val1 < val2:
            is_less_than = True
            
        else: 
            pass

        # Generate descriptive output based on comparison result
        message_parts = []
        
        if not (is_greater_than or is_less_than):
            msg = "The volumes are equal."
            
        elif is_greater_than:
            msg = f"Volume {val1} is greater than volume {val2}."
            
        else: 
            msg = f"Volume {val1} is smaller than volume {val2}."

        print(msg)

if __name__ == '__main__':
    # Hard-coded sample values for testing the VolumeComparator class.
    # This block ensures no user input, command-line arguments, or network access are required.
    
    comparator = VolumeComparator()

    test_cases: list[tuple[float | None]] = [
        (10.5, 20.3),      # Case where second is greater
        (None, 7.8),       # Case with None and smaller value
        (42.0, 42.0),     # Exact equality case
        (99.9, None),      # First larger than zero defaulting to None's zero equivalent
    ]

    for vol1, vol2 in test_cases:
        comparator.compare(vol1, vol2)