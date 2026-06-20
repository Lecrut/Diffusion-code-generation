class DistanceConverter:
    MILES_TO_KM = 1.60934
    KM_TO_MILES = 1 / 1.60934

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()

        if not isinstance(self.value, (int, float)):
            raise ValueError("Value must be numeric.")
        if self.unit not in ('miles', 'km', 'kilometers'):
            raise ValueError("Unit must be 'miles', 'km', or 'kilometers'.")

    def to_km(self):
        if self.unit == 'miles':
            return self.value * self.MILES_TO_KM
        return self.value

    def to_miles(self):
        if self.unit in ('km', 'kilometers'):
            return self.value * self.KM_TO_MILES
        return self.value

    def convert(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit == 'miles':
            return self.to_miles()
        elif target_unit in ('km', 'kilometers'):
            return self.to_km()
        else:
            raise ValueError("Target unit must be 'miles', 'km', or 'kilometers'.")

if __name__ == '__main__':
    converter = DistanceConverter(10, 'miles')
    km_result = converter.to_km()
    print(km_result)

    miles_result = converter.convert('miles')
    print(miles_result)

    km_converter = DistanceConverter(10, 'km')
    miles_from_km = km_converter.to_miles()
    print(miles_from_km)