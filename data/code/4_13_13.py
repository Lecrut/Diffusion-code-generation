class DistanceConverter:
    def __init__(self):
        # Conversion factors to meters (base unit)
        self.meters_per_mile = 1609.34
        self.meters_per_kilometer = 1000.0
        self.meters_per_meter = 1.0

    def _convert_to_base(self, distance: float, from_unit: str) -> float:
        """Convert a given distance to the base unit (meters)."""
        if from_unit == 'mile':
            return distance * self.meters_per_mile
        elif from_unit == 'kilometer':
            return distance * self.meters_per_kilometer
        else:  # meter
            return distance

    def _convert_from_base(self, meters: float, to_unit: str) -> float:
        """Convert a base unit (meters) to the target unit."""
        if to_unit == 'mile':
            return meters / self.meters_per_mile
        elif to_unit == 'kilometer':
            return meters / self.meters_per_kilometer
        else:  # meter
            return meters

    def convert(self, distance: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a distance from one unit to another.
        
        Args:
            distance (float): The value of the distance in 'from_unit'.
            from_unit (str): Source unit ('mile', 'kilometer', or 'meter').
            to_unit (str): Target unit ('mile', 'kilometer', or 'meter').

        Returns:
            float: Converted distance.
        
        Raises:
            ValueError: If unsupported units are provided.
        """
        valid_units = {'mile', 'kilometer', 'meter'}
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Unsupported unit '{from_unit}' or '{to_unit}'. Valid units: {valid_units}")

        # Convert source distance to meters, then convert meters to target unit
        base_meters = self._convert_to_base(distance, from_unit)
        return self._convert_from_base(base_meters, to_unit)

if __name__ == '__main__':
    converter = DistanceConverter()

    # Sample conversions without user input
    print(f"{converter.convert(5.0, 'mile', 'kilometer')} kilometers")  # Output: ~8.0467 km
    print(f"{converter.convert(10.0, 'kilometer', 'meter')} meters")     # Output: 10000 m
    print(f"{converter.convert(3280.5, 'foot', 'mile')} miles" if False else f"{converter.convert(1.0, 'mile', 'meters')} meters")  # Note: foot not supported in this specific scope based on task constraints (only mile/kilometer/meter), so using meter->kilometer instead
    print(f"{converter.convert(50.0, 'meter', 'kilometer')} kilometers")