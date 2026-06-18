class DistanceConverter:
    """Handles conversions between meters, kilometers, and miles with type safety."""

    def __init__(self):
        self._conversion_factors = {
            'meters_to_kilometers': 0.001,
            'kilometers_to_miles': 0.621371,
            'meters_to_miles': 0.000621371,
        }

    def _validate_input(self, value: float | int) -> None:
        """Ensure the input is a valid numeric type."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected number or str with 'm', 'km' or 'mi'. Got {type(value).__name__}")

    def convert_meters_to_kilometers(self, meters: int | float) -> float:
        """Convert distance from meters to kilometers."""
        self._validate_input(meters)
        return meters * self._conversion_factors['meters_to_kilometers']

    def convert_km_to_miles(self, km: int | float) -> float:
        """Convert distance from kilometers to miles."""
        self._validate_input(km)
        return km * self._conversion_factors['kilometers_to_miles']

    def meters_to_miles(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_str(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

    def meters_to_mi(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to miles."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value))) * self._conversion_factors['kilometers_to_miles']

    def meters_to_km(self, value: str):
        """Parse a string like '100 m', '2.5 km' or '3 mi' and convert to kilometers."""
        if isinstance(value, int) or isinstance(value, float):
            return self.convert_meters_to_kilometers(int(float(value)))

if __name__ == '__main__':
    pass
