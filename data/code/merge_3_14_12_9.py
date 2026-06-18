class VolumeComparator:
    """A professional class designed to compare two volume measurements."""

    def __init__(self):
        self._comparison_count = 0

    @staticmethod
    def _format_message(volume1, unit1, volume2, unit2, result_type):
        """Generate a descriptive string based on the comparison result.

        Args:
            volume1 (float): First measured value.
            unit1 (str): Unit of the first measurement.
            volume2 (float): Second measured value.
            unit2 (str): Unit of the second measurement.
            result_type (str): Type of relationship ('greater', 'smaller', 'equal').

        Returns:
            str: A formatted descriptive string indicating the comparison outcome.
        """
        messages = {
            'greater': f"{volume1} ({unit1}) is greater than {volume2} ({unit2}).",
            'smaller': f"{volume1} ({unit1}) is smaller than {volume2} ({unit2}).",
            'equal': f"{volume1} ({unit1}) is equal to {volume2} ({unit2})."
        }

        return messages.get(result_type, "Comparison could not be determined.")

    def compare(self, volume1: float, unit1: str, volume2: float, unit2: str) -> None:
        """Compare two volumes and print a descriptive result.

        This method performs an efficient numerical comparison between 
        `volume1` (in `unit1`) and `volume2` (in `unit2`). It assumes 
        the units are compatible for direct numeric comparison as per standard 
        practice in such utility classes unless unit conversion logic is explicitly required.
        
        Args:
            volume1 (float): The first numerical value representing a volume.
            unit1 (str): The string representation of the unit for the first volume.
            volume2 (float): The second numerical value representing a volume.
            unit2 (str): The string representation of the unit for the second volume.

        Returns:
            None: Prints the result directly to standard output.
        
        Raises:
            TypeError: If inputs are not numeric or units are missing strings.
        """
        if not isinstance(volume1, (int, float)) or not isinstance(volume2, (int, float)):
            raise TypeError("Volume arguments must be numeric.")
        if not unit1.strip() or not unit2.strip():
            raise ValueError("Unit arguments cannot be empty strings.")

        self._comparison_count += 1
        
        comparison_result = 'equal'
        
        # Handle floating point precision issues by using a small epsilon for equality check
        EPSILON = 1e-9
        
        if volume1 > (volume2 + EPSILON):
            comparison_result = 'greater'
        elif volume1 < (volume2 - EPSILON):
            comparison_result = 'smaller'

        message = self._format_message(volume1, unit1.strip(), volume2, unit2.strip(), comparison_result)
        print(message)

if __name__ == '__main__':
    # Initialize the comparator instance
    vc = VolumeComparator()

    # Hard-coded sample values for testing without user input or external dependencies
    vol_a = 5.0
    unit_a = "liters"
    
    vol_b = 12.4
    unit_b = "gallons"

    # Example comparison scenario
    vc.compare(vol_a, unit_a, vol_b, unit_b)

    # Additional test case for equality (using integers to avoid float precision issues in demo)
    vc.compare(30, "kg", 30, "kilograms")