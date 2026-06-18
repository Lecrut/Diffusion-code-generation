class DistanceConverter:
    """
    A class to handle conversions between meters (m), kilometers (km), and miles (mi).
    
    Constants defined based on standard conversion factors:
    1 km = 1000 m
    1 mi = 1609.344 m
    
    Attributes:
        None
        
    Methods:
        convert_to_meters(distance, from_unit) -> float: Convert any unit to meters.
        convert_from_meters(meter_distance, to_unit) -> str: Get a formatted string of the converted distance.
    
    Example usage (not shown here as per task constraints for comments):
        converter = DistanceConverter()
        result = converter.convert_to_meters(5000, 'km')  # Returns 5000000.0
        
        print(converter.convert_from_meters(result, 'mi')) 
    """

    def __init__(self) -> None:
        """Initializes the DistanceConverter instance with no parameters."""
        pass

    @staticmethod
    def _validate_unit(unit: str) -> bool:
        """Checks if the provided unit is supported (m, km, mi)."""
        return unit.lower() in ['m', 'km', 'mi']

    # --- Conversion Logic ---

    # Converts a distance from any of m/km/mi to meters.
    def convert_to_meters(self, distance: float | int, from_unit: str) -> float:
        """
        Converts the specified distance into meters based on the input unit.
        
        Args:
            distance (float|int): The value to be converted.
            from_unit (str): The source unit ('m', 'km', or 'mi'). Must be lowercase for case-insensitive handling, 
                             though strictly typed here as string match against expected values.
                             
        Returns:
            float: The equivalent distance in meters. Raises ValueError if the unit is invalid.
            
        Examples:
            >>> converter.convert_to_meters(1000, 'km')
            1000000.0
            >>> converter.convert_to_meters(5, 'mi')
            8046.72
        """
        if not self._validate_unit(from_unit):
            raise ValueError(f"Unsupported unit: {from_unit}. Supported units are m, km, mi.")

        # Ensure distance is numeric (float) for internal calculation consistency
        dist = float(distance)

        meters_per_km = 1000.0
        meters_per_mi = 1609.344

        if from_unit == 'km':
            return dist * meters_per_km
        elif from_unit == 'mi':
            return dist * meters_per_mi
        else: # Unit is 'm' or case-insensitive match for m
            return float(dist)

    # Converts a distance in meters to the target unit and returns a formatted string.
    def convert_from_meters(self, meter_distance: float | int, to_unit: str) -> str:
        """
        Returns the input distance converted from meters to the specified target unit as a formatted string.
        
        Args:
            meter_distance (float|int): The value in meters.
            to_unit (str): The target unit ('m', 'km', or 'mi'). Must be lowercase.
                             
        Returns:
            str: A human-readable string representation of the converted distance with appropriate precision and suffix.
            
        Examples:
            >>> converter.convert_from_meters(5000, 'm')
            "5000 meters"
            >>> converter.convert_from_meters(1609344, 'mi')
            "1 miles" (Note: Integer handling might drop decimals for cleaner output in this specific implementation choice)
        """
        if not self._validate_unit(to_unit):
            raise ValueError(f"Unsupported target unit: {to_unit}. Supported units are m, km, mi.")

        distance = float(meter_distance)
        
        # Formatting logic to avoid excessive decimal places for meters while keeping precision for others

if __name__ == '__main__':
    pass
