class DistanceConverter:
    MILES_TO_KM_FACTOR = 1.609344
    KM_TO_MILES_FACTOR = 0.621371192

    def __init__(self):
        self._factors = {
            ('miles', 'kilometers'): self.MILES_TO_KM_FACTOR,
            ('kilometers', 'miles'): self.KM_TO_MILES_FACTOR
        }

    def _validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Distance value must be numeric.")
        if value < 0:
            raise ValueError("Distance cannot be negative.")
        return float(value)

    def convert(self, distance, from_unit, to_unit):
        validated_distance = self._validate_input(distance)
        normalized_from = from_unit.lower()
        normalized_to = to_unit.lower()

        if normalized_from == normalized_to:
            return validated_distance

        factor = self._factors.get((normalized_from, normalized_to))

        if factor is None:
            raise ValueError("Unsupported unit conversion pair.")

        return validated_distance * factor

if __name__ == '__main__':
    converter = DistanceConverter()

    sample_miles = 100
    sample_km = 100

    result_km = converter.convert(sample_miles, 'miles', 'kilometers')
    print(f"{sample_miles} miles is {result_km} kilometers")

    result_miles = converter.convert(sample_km, 'kilometers', 'miles')
    print(f"{sample_km} kilometers is {result_miles} miles")

    try:
        converter.convert("abc", 'miles', 'kilometers')
    except TypeError as e:
        print(f"Caught expected TypeError: {e}")

    try:
        converter.convert(-5, 'miles', 'kilometers')
    except ValueError as e:
        print(f"Caught expected ValueError: {e}")