"""
Module to normalize arbitrary distance measurements into meters.
Handles various units including kilometers, centimeters, millimeters, 
micrometers, nanometers, light-years, astronomical units, etc., 
using standard conversion factors relative to the meter (SI base unit).
"""

class DistanceNormalizer:
    """A class to convert any supported distance measurement into meters."""

    # Conversion multipliers from each specific unit to 1 meter.
    # Positive value means multiply by this factor; negative implies division logic handled separately if needed,
    # but here all are direct multiplicative factors for the target 'meter'.
    
    UNIT_FACTORS = {
        "meters": 1.0,
        "kilometers": 1_000.0,      # km * 10^3 -> m
        "centimeters": 1e-2,         # cm / 10^2 (or multiply by 0.01)
        "millimeters": 1e-3,         # mm / 10^3
        "micrometers": 1e-6,         # um / 10^6
        "nanometers": 1e-9,          # nm / 10^9
        "light-years": 9.4607304725808e+15, 
        "astronomical-units": 1.49597870691e+11,
    }

    def __init__(self):
        """Initialize the normalizer with empty conversion history."""
        self.history = []

    def normalize(self, value: float, unit: str) -> float:
        """
        Convert a distance measurement to meters.

        Args:
            value (float): The magnitude of the distance.
            unit (str): The source unit string (case-insensitive). Supported units are defined in UNIT_FACTORS.

        Returns:
            float: Distance normalized into meters rounded for readability but preserving precision where necessary.
        
        Raises:
            ValueError: If an unsupported unit is provided or value is not numeric.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")

        # Normalize string input to lowercase and remove hyphens for dictionary lookup consistency
        normalized_unit = str(unit).strip().lower().replace("-", "_")
        
        factor = self.UNIT_FACTORS.get(normalized_unit)
        if not factor:
            raise ValueError(f"Unsupported unit '{unit}'. Available units are {list(self.UNIT_FACTORS.keys())}.")

        meters = value * factor
        
        # Round to avoid floating point artifacts for very large/small numbers unless they exceed standard float precision limits significantly, 
        # though Python floats generally handle scientific notation well enough for most practical distance calculations.
        
        return round(meters, 10)

def main():
    """Main execution block with hard-coded sample values."""
    
    normalizer = DistanceNormalizer()

    test_cases = [
        ("5", "kilometers"),       # Expected: ~5000 m
        (1.234e9, "nanometers"),  # Expected: ~1.234 m
        (-100, "centimeters"),    # Negative distance is physically weird but mathematically valid for normalization: -1 m
        ("864", "light-years"),   # Huge number expected in meters
        (5e-9, "micrometers"),    # Small positive: 5e-3 mm -> 0.000005 m? No wait: um * 1e-6 = 5e-12 m. Let's recheck logic below manually if needed.
        ("4", "astronomical-units") 
    ]

    print("Distance Normalization to Meters:")
    print("-" * 30)

    for value_str, unit in test_cases:
        try:
            val = float(value_str)
            result_meters = normalizer.normalize(val, unit)
            
            # Display original input and calculated meters with scientific notation if needed to keep it clean but readable. 
            # Python's default str(float) handles this well for most cases including large/small numbers.
            print(f"Input: {val} {unit}")
            print(f"Result in Meters: {result_meters:.15e}\n")

        except ValueError as ve:
            print(f"Error processing '{value_str}' with unit '{unit}': {ve}\n")

if __name__ == '__main__':
    main()