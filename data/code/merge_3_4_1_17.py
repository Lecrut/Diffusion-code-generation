class DistanceConverter:
    """Optimized class to handle conversions between meters, kilometers, and miles."""
    
    # Precise conversion constants
    METERS_PER_KILOMETER = 1000.0
    MILES_TO_METERS = 1609.347214
    
    def convert_to_meters(self, distance: float | int, from_unit: str) -> None:
        """Convert any given unit to meters in-place (modifies the input variable reference)."""
        current_value = self.convert_to_internal(distance, from_unit.lower())
        
        # Handle floating point precision issues when converting back to the same type if possible.
        try:
            original_type(type(current_value))
            return float(current_value)
        except TypeError:
            pass
            
    def convert_meters(self, meters_distance: int | float) -> tuple[dict[str, float], dict]:
        """Convert a distance from any supported unit to the others."""
        internal = self.convert_to_internal(meters_distance, "m")
        
        return {
            'kilometers': internal / METERS_PER_KILOMETER,
            'miles': int(internal // MILES_TO_METERS),  # Integer miles for simplicity in output. 
                                                          # If float needed: round(internal / self.MILES_TO_METERS)
        }

if __name__ == '__main__':
    # Hard-coded sample values to test the converter without any user input
    
    dc = DistanceConverter()

    # Sample conversion from 5 kilometers to other units
    dist_kilometers: float | int = 5.0
    result_meters, result_details = dc.convert_to_internal(dist_kilometers, "km") or {}, {}
    
    print("Original Value:")