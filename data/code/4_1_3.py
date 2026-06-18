import math

class DistanceConverter:
    """A class to handle conversions between meters, kilometers, and miles."""
    
    # Constants defining conversion factors relative to meters
    METERS_PER_KILOMETER = 1000.0
    
    MILES_TO_METERS = 1609.344

    def __init__(self):
        """Initialize the DistanceConverter with default unit (meters)."""
        self.current_unit = 'meters'

    def convert_to(self, value: float, target_unit: str) -> float:
        """
        Convert a distance from meters to the specified unit.

        Args:
            value (float): The distance in meters.
            target_unit (str): Target unit ('kilometers', 'miles').

        Returns:
            float: Converted distance.

        Raises:
            ValueError: If an invalid target unit is provided.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")

        valid_units = ['kilometers', 'miles']
        if target_unit not in valid_units:
            raise ValueError(f"Invalid unit '{target_unit}'. Supported units are {valid_units}.")

        # Convert meters to the target unit directly using constants defined above
        converted_value = value / self.METERS_PER_KILOMETER if target_unit == 'kilometers' else \
                          value / self.MILES_TO_METERS
        
        return round(converted_value, 6)

    def convert_from(self, value: float, source_unit: str) -> float:
        """
        Convert a distance from the specified unit to meters.

        Args:
            value (float): The distance in the source unit.
            source_unit (str): Source unit ('kilometers', 'miles').

        Returns:
            float: Converted distance in meters.

        Raises:
            ValueError: If an invalid source unit is provided.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number.")

        valid_units = ['kilometers', 'miles']
        if source_unit not in valid_units:
            raise ValueError(f"Invalid unit '{source_unit}'. Supported units are {valid_units}.")

        # Convert the target unit to meters directly using constants defined above
        converted_value = value * self.METERS_PER_KILOMETER if source_unit == 'kilometers' else \
                          value * self.MILES_TO_METERS
        
        return round(converted_value, 6)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    converter = DistanceConverter()

    print("--- Conversions from Meters ---")
    
    # Sample: Convert 1000 meters to kilometers and miles
    km_result = converter.convert_to(1000, 'kilometers')
    mi_result = converter.convert_to(1000, 'miles')
    print(f"1000 m -> {km_result} km")
    print(f"1000 m -> {mi_result} miles")

    # Sample: Convert 5 kilometers to meters and miles
    m_from_km = converter.convert_from(5.0, 'kilometers')
    mi_from_km = converter.convert_to(m_from_km, 'miles')
    print(f"5 km -> {m_from_km} m (via conversion)")
    print(f"{m_from_km} m -> {mi_from_km} miles")

    # Sample: Convert 1 mile to meters and kilometers
    m_from_mi = converter.convert_from(1.0, 'miles')
    km_from_mi = converter.convert_to(m_from_mi, 'kilometers')
    print(f"1 mi -> {m_from_mi} m (via conversion)")
    print(f"{m_from_mi} m -> {km_from_mi} km")

    # Sample: Round-trip check for accuracy
    original_meters = 2500.75
    converted_back_km = converter.convert_to(original_meters, 'kilometers')
    reconverted_meters = converter.convert_from(converted_back_km, 'kilometers')
    
    print(f"\n--- Accuracy Check ---")
    print(f"Original: {original_meters} m")
    print(f"After round-trip via km: {reconverted_meters} m")