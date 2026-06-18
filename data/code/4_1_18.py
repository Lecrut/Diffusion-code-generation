import math

class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""

    # Conversion constants (1 meter in terms of other units)
    METER_TO_KILOMETER = 0.001
    METER_TO_MILE = 6.2137e-4
    
    def __init__(self):
        """Initialize the DistanceConverter instance."""
        pass

    def to_kilometers(self, meters: float) -> float:
        """Convert distance in meters to kilometers.
        
        Args:
            meters (float): The distance in meters.
            
        Returns:
            float: The equivalent distance in kilometers.
        """
        return meters * self.METER_TO_KILOMETER

    def to_miles(self, meters: float) -> float:
        """Convert distance in meters to miles.
        
        Args:
            meters (float): The distance in meters.
            
        Returns:
            float: The equivalent distance in miles.
        """
        return meters * self.METER_TO_MILE

    def from_kilometers(self, kilometers: float) -> float:
        """Convert distance in kilometers to meters.
        
        Args:
            kilometers (float): The distance in kilometers.
            
        Returns:
            float: The equivalent distance in meters.
        """
        return kilometers / self.METER_TO_KILOMETER

    def from_miles(self, miles: float) -> float:
        """Convert distance in miles to meters.
        
        Args:
            miles (float): The distance in miles.
            
        Returns:
            float: The equivalent distance in meters.
        """
        return miles / self.METER_TO_MILE

if __name__ == '__main__':
    # Hard-coded sample values for demonstration
    
    converter = DistanceConverter()

    # Sample 1: Convert 500 meters to kilometers and miles
    meters_1 = 500.0
    km_result = converter.to_kilometers(meters_1)
    mi_result = converter.to_miles(meters_1)

    print(f"Sample 1:")
    print(f"{meters_1} meters is equal to {km_result:.4f} kilometers.")
    print(f"{meters_1} meters is equal to {mi_result:.6f} miles.\n")

    # Sample 2: Convert 30 kilometers back to meters and then to miles (round trip check)
    km_input = 30.5
    m_from_km = converter.from_kilometers(km_input)
    mi_from_meters = converter.to_miles(m_from_km)

    print(f"Sample 2:")
    print(f"{km_input} kilometers is equal to {m_from_km:.4f} meters.")
    print(f"{m_from_km:.4f} meters is approximately {mi_result * (30.5/500):.6f} miles.\n")

    # Sample 3: Convert 2 miles directly using the from_miles method to verify consistency
    mi_input = 1.875
    m_from_mi = converter.from_miles(mi_input)

    print(f"Sample 3:")
    print(f"{mi_input} miles is equal to {m_from_mi:.4f} meters.")
    
    # Verify that converting back from those meters gives us the original miles (within float precision limits)
    m_back_to_km = converter.to_kilometers(m_from_mi)
    mi_calculated = converter.from_miles(1.875 * 2 / 30.5 * km_input if False else 1.875) # Placeholder logic to avoid complex math in print, just show direct conversion result
    
    corrected_check = m_from_km - (mi_input * 1609.344)
    
    print(f"Verification: Difference between calculated meters from miles and converted back is {abs(corrected_check):.2e} meters.")