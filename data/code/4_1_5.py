import math

class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""

    # Constants defining conversion rates relative to a base unit (meters)
    METERS_PER_METER = 1.0
    KILOMETERS_TO_METERS = 1000.0
    MILES_TO_METERS = 1609.347214

    def __init__(self, value: float | int):
        """Initialize the converter with a distance in meters."""
        if not isinstance(value, (int, float)):
            raise TypeError("Distance must be an integer or float.")
        self.value_meters = float(value)

    def to_kilometers(self) -> float:
        """Convert current value from meters to kilometers.

        Returns:
            Distance in kilometers as a float.
        """
        return self.value_meters / self.KILOMETERS_TO_METERS

    def to_miles(self) -> float:
        """Convert current value from meters to miles.

        Returns:
            Distance in miles as a float.
        """
        return self.value_meters / self.MILES_TO_METERS

    def __repr__(self):
        """Return a string representation of the object."""
        return f"DistanceConverter({self.value_meters} meters)"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample 1: Convert standard distances
    run = DistanceConverter(402.3)          # Standard track length in meters
    swim_lap = DistanceConverter(50.0)      # Lap length in meters

    print(f"Running {run}m is equal to:")
    print(f"{run.to_kilometers():.6f} km")
    print(f"{run.to_miles():.8f} miles\n")

    swim_lap_print = f"A 50m lap ({swim_lap}) converts to:"
    print(swim_lap_print)
    print(f"   {swim_lap.to_kilometers():.6f} km")
    print(f"   {swim_lap.to_miles():.8f} miles\n")

    # Sample 2: Verify type safety and edge cases
    try:
        invalid = DistanceConverter("100")
    except TypeError as e:
        print(f"Caught expected error for non-numeric input: {e}\n")

    # Large distance calculation check (approximate marathon)
    marathon_meters = 42195.0
    marathon_conv = DistanceConverter(marathon_meters)
    
    print("Marathon distance verification:")
    print(f"Input meters: {marathon_meters}")
    print(f"Converted to km: {marathon_conv.to_kilometers():.6f} (Expected ~42.195)")
    assert abs(marathon_conv.to_kilometers() - 42.195) < 0.001, "Conversion accuracy check failed."
    
    print("\nAll tests passed successfully.")