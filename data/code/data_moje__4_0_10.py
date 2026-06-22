class DistanceConverter:
    def __init__(self, value, unit):
        valid_units = ['meters', 'kilometers', 'miles']
        if unit.lower() not in valid_units:
            raise ValueError(f"Unit must be one of: {valid_units}")
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        if value < 0:
            raise ValueError("Value cannot be negative")
        self.value = float(value)
        self.unit = unit.lower()

    def convert_to(self, target_unit):
        target_unit = target_unit.lower()
        valid_units = ['meters', 'kilometers', 'miles']
        if target_unit not in valid_units:
            raise ValueError(f"Target unit must be one of: {valid_units}")
        
        if self.unit == target_unit:
            return self.value

        meters = 0.0
        if self.unit == 'meters':
            meters = self.value
        elif self.unit == 'kilometers':
            meters = self.value * 1000
        elif self.unit == 'miles':
            meters = self.value * 1609.344

        if target_unit == 'meters':
            return meters
        elif target_unit == 'kilometers':
            return meters / 1000
        elif target_unit == 'miles':
            return meters / 1609.344

if __name__ == '__main__':
    converter = DistanceConverter(5, 'kilometers')
    miles_result = converter.convert_to('miles')
    meters_result = converter.convert_to('meters')
    print(miles_result)
    print(meters_result)
    converter_miles = DistanceConverter(3, 'miles')
    km_result = converter_miles.convert_to('kilometers')
    print(km_result)