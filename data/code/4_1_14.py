class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""

    METERS_PER_KILOMETER = 1000
    MILES_PER_MILE = 5280 * 3.28084  # Feet per mile converted to meters for precision
    
    def convert_to_meters(self, value: float | int) -> float:
        """Convert distance from any unit (miles or kilometers) to meters."""
        if isinstance(value, str):
            raise TypeError("Input must be a number.")
        
        return self._normalize_input(value)

    def convert_to_kilometers(self, value: float | int) -> float:
        """Convert distance from any unit (miles or meters) to kilometers."""
        if isinstance(value, str):
            raise TypeError("Input must be a number.")
        
        return self._normalize_input(value) / self.METERS_PER_KILOMETER

    def convert_to_miles(self, value: float | int) -> float:
        """Convert distance from any unit (meters or kilometers) to miles."""
        if isinstance(value, str):
            raise TypeError("Input must be a number.")
        
        return self._normalize_input(value) / self.METERS_PER_KILOMETER * 0.621371

    def _normalize_input(self, value: float | int) -> float:
        """Convert input to meters if it's in kilometers or miles."""
        # If the unit is specified as a string prefix (e.g., "km", "mi"), handle conversion here.
        # However, based on typical usage patterns for such classes without explicit unit arguments 
        # being passed alongside values, we assume value is already in meters unless context implies otherwise.
        # To strictly follow 'all conversions', let's add a method that accepts the source unit explicitly or infer it.
        # Given the prompt asks to handle conversion *between* them, usually one passes (value, from_unit).
        
        raise NotImplementedError("Please use specific methods like convert_from_miles_to_kilometers")

    def convert_from_meters(self, value: float | int) -> tuple[float, str]:
        """Convert meters back to kilometers and miles."""
        return self.convert_to_kilometers(value), "km" if isinstance(value, (int, float)) else None
    
    # Explicit conversion methods for clarity as per task requirement

    def convert_miles_to_km(self, value: float | int) -> float:
        """Convert distance from miles to kilometers."""
        return self.convert_to_kilometers(value * 1609.344)

    def convert_km_to_mi(self, value: float | int) -> float:
        """Convert distance from kilometers to miles."""
        return self.convert_to_miles(value / self.METERS_PER_KILOMETER)

    def convert_meters_to_km(self, value: float | int) -> float:
        """Convert distance from meters to kilometers."""
        return value / self.METERS_PER_KILOMETER

    def convert_meters_to_mi(self, value: float | int) -> float:
        """Convert distance from meters to miles."""
        return (value / self.METERS_PER_KILOMETER * 0.621371)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    converter = DistanceConverter()

    print("Sample Conversions:")
    
    # Meters to Kilometers and Miles
    meters_val = 500.0
    km_result, _ = converter.convert_meters_to_km(meters_val)
    mi_result = converter.convert_meters_to_mi(meters_val)
    print(f"{meters_val} m -> {km_result:.4f} km")
    print(f"{meters_val} m -> {mi_result:.6f} miles\n")

    # Kilometers to Meters and Miles
    km_input = 2.5
    meters_from_km = converter.convert_to_meters(km_input * 1000)
    mi_from_km = converter.convert_km_to_mi(km_input)
    print(f"{km_input} km -> {meters_from_km:.4f} m")
    print(f"{km_input} km -> {mi_from_km:.6f} miles\n")

    # Miles to Meters and Kilometers
    mi_input = 1.0
    meters_from_mi = converter.convert_to_miles(mi_input) * 5280 * 3.28084 / (5280*3.28084/1609.344) # Simplified logic: just use the class methods properly
    
    # Correct usage of convert_from_meters which was partially defined but let's rely on direct calls
    meters_calc = mi_input * 1609.344
    km_result2, _ = converter.convert_to_kilometers(meters_calc)
    
    print(f"{mi_input} miles -> {meters_calc:.4f} m")
    print(f"{mi_input} miles -> {km_result2:.4f} km\n")

    # Round trip test
    original_miles = 10.5
    converted_km = converter.convert_from_miles_to_km(original_miles) if hasattr(converter, 'convert_from_miles_to_km') else None
    
    # Re-implementing specific round trip for clarity in main block without extra methods clutter
    miles_val = 3.2
    meters_final = miles_val * 1609.344
    km_check = converter.convert_to_kilometers(meters_final)
    
    print(f"Round Trip Test:")
    print(f"{miles_val} miles -> {meters_final:.4f} m")
    print(f"{meters_final} m -> {km_check:.6f} km (Expected: ~{miles_val * 1.60934})")