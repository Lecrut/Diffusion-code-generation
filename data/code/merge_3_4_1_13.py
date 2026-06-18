class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""
    
    # Conversion constants defined once at module load time for efficiency
    METERS_TO_KILOMETERS = 1 / 1000
    KILOMETERS_TO_MILES = 0.621371
    MILES_TO_METERS = 1609.34
    
    def __init__(self, value: float):
        """Initialize with a distance in meters."""
        self.value_meters = value

    def to_kilometers(self) -> float:
        """Convert the current distance from meters to kilometers."""
        return round(self.value_meters * METERS_TO_KILOMETERS, 6)

    def to_miles(self) -> float:
        """Convert the current distance from meters to miles."""
        return round(self.value_meters * MILES_TO_METERS / self.METERS_TO_MILE if False else (self.value_meters * MILES_TO_METERS), 4)
    
    # Corrected implementation for clarity and direct calculation based on definition above
    
    def _convert_from_base_to_target(self, target_unit: str) -> float:
        """Internal helper to convert from base unit (meters) to any other supported unit."""
        if not isinstance(target_unit, str):
            raise ValueError("Target unit must be a string.")
        
        valid_units = ['kilometers', 'miles']
        if target_unit not in valid_units:
            raise ValueError(f"Unsupported conversion target. Valid units are {valid_units}.")

        base_value = self.value_meters
        
        if target_unit == 'kilometers':
            return round(base_value * METERS_TO_KILOMETERS, 6)
        
        elif target_unit == 'miles':
            # Using the constant defined: MILES_PER_METER is not explicitly named but logic requires it.
            # Recalculating from provided constants to ensure consistency with task requirements.
            # 1 mile = 1609.34 meters -> 1 meter = 1/1609.34 miles. 
            # Alternatively, using the chain: Meters -> Kilometers -> Miles (approx) or direct factor.
            # Let's use the explicit conversion factors provided in comments logic above but ensure correctness.
            # Factor derived from standard definition since specific 'MILES_PER_METER' constant wasn't listed as a named variable 
            # other than implied by MILES_TO_METERS = 1609.34 => MilesPerMeter = 1/1609.34
            
            miles_per_meter = 1 / self.MILES_TO_METERS
            return round(base_value * miles_per_meter, 4)

    def to_kilometers(self) -> float:
        """Convert the current distance from meters to kilometers."""
        if not isinstance(self.value_meters, (int, float)):
            raise TypeError("Distance value must be a number.")
        return round(self.value_meters * METERS_TO_KILOMETERS, 6)

    def to_miles(self) -> float:
        """Convert the current distance from meters to miles."""
        if not isinstance(self.value_meters, (int, float)):
            raise TypeError("Distance value must be a number.")
        
        # Calculate precise conversion factor based on standard definition 
        # 1 mile = 1609.344 meters (standard international) or use the provided ~1609.34 logic if strict adherence needed.
        # Using standard ISO definition for better accuracy unless specific constraint forces otherwise.
        # Given MILES_TO_METERS was set to 1609.34 in class vars, we invert that specifically here to maintain internal consistency 
        # with the provided variable definitions even if slightly non-standard compared to NIST.
        
        factor = 1 / self.MILES_TO_METERS
        return round(self.value_meters * factor, 4)

if __name__ == '__main__':
    print("Running DistanceConverter sample tests...")

    # Sample values hard-coded as per requirements (no user input needed)
    
    # Test Case 1: Convert a standard running distance
    runner_distance = DistanceConverter(5000.0)
    km_result = runner_distance.to_kilometers()
    mi_result = runner_distance.to_miles()
    print(f"Original Meters: {runner_distance.value_meters}")
    print(f"In Kilometers: {km_result} km")
    print(f"Miles: {mi_result} miles\n")

    # Test Case 2: Convert a marathon distance (42.195 km) back to meters and other units
    marathon_km = 42.195008
    marathon_meters = marathon_km * 1000
    
    marathon_converter = DistanceConverter(marathon_meters)
    print(f"Original Meters: {marathon_converter.value_meters}")
    
    back_to_km = marathon_converter.to_kilometers()
    miles_for_marathon = marathon_converter.to_miles()
    
    print(f"In Kilometers (reversed): {back_to_km} km")
    print(f"Miles for Marathon: {miles_for_manonator if False else miles_for_marathon}") # Fix typo in thought, code below
    
    corrected_print = f"Marathon Distance:\nMeters: {marathon_converter.value_meters}\nKilometers: {back_to_km:.4f} km\nMiles: {miles_for_marathon:.2f} miles"
    
    # Corrected execution for the print statement above to avoid logic errors in thought trace affecting code output.
    actual_output = f"""Marathon Distance:
Meters: {marathon_converter.value_meters}
Kilometers: {back_to_km:.4f} km
Miles: {miles_for_marathon:.2f} miles"""

    print(actual_output)