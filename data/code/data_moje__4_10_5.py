class DistanceConverter:
    MILES_TO_KILOMETERS = 1.609344
    KILOMETERS_TO_MILES = 0.621371192237334

    def __init__(self):
        self._miles_to_km = self.MILES_TO_KILOMETERS
        self._km_to_miles = self.KILOMETERS_TO_MILES

    def _validate_numeric(self, value):
        if isinstance(value, bool):
            raise TypeError("Boolean values are not accepted as numeric input")
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected numeric type, got {type(value).__name__}")
        return value

    def _validate_non_negative(self, value):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        return value

    def miles_to_kilometers(self, miles):
        checked_value = self._validate_numeric(miles)
        self._validate_non_negative(checked_value)
        return checked_value * self._miles_to_km

    def kilometers_to_miles(self, kilometers):
        checked_value = self._validate_numeric(kilometers)
        self._validate_non_negative(checked_value)
        return checked_value * self._km_to_miles

    def convert(self, distance, from_unit, to_unit):
        if from_unit is None or to_unit is None:
            raise ValueError("Unit strings cannot be None")
        from_lower = from_unit.lower().strip()
        to_lower = to_unit.lower().strip()
        
        if from_lower not in ['mile', 'miles', 'km', 'kilometer', 'kilometers']:
            raise ValueError(f"Invalid source unit: {from_unit}")
        if to_lower not in ['mile', 'miles', 'km', 'kilometer', 'kilometers']:
            raise ValueError(f"Invalid target unit: {to_unit}")

        if from_lower == to_lower:
            self._validate_numeric(distance)
            return self._validate_non_negative(distance)

        is_miles_to_km = (from_lower in ['mile', 'miles']) and (to_lower in ['km', 'kilometer', 'kilometers'])
        is_km_to_miles = (from_lower in ['km', 'kilometer', 'kilometers']) and (to_lower in ['mile', 'miles'])

        if not is_miles_to_km and not is_km_to_miles:
            raise ValueError("Incompatible unit conversion requested")

        if is_miles_to_km:
            return self.miles_to_kilometers(distance)
        else:
            return self.kilometers_to_miles(distance)

if __name__ == '__main__':
    converter = DistanceConverter()
    sample_miles = 10.5
    sample_km = 50.0
    converted_km = converter.miles_to_kilometers(sample_miles)
    converted_miles = converter.kilometers_to_miles(sample_km)
    mixed_convert_1 = converter.convert(100, "miles", "km")
    mixed_convert_2 = converter.convert(160.9344, "kilometers", "miles")
    print(f"{sample_miles} miles is {converted_km} kilometers")
    print(f"{sample_km} kilometers is {converted_miles} miles")
    print(f"100 miles equals {mixed_convert_1} kilometers")
    print(f"160.9344 kilometers equals {mixed_convert_2} miles")