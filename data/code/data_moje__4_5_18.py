class DistanceConverter:
    def __init__(self):
        self.units = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'mi': 1609.344,
            'yd': 0.9144,
            'ft': 0.3048,
            'in': 0.0254
        }

    def convert(self, distance, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in self.units:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        if distance < 0:
            raise ValueError("Distance cannot be negative")

        meters = distance * self.units[from_unit]
        result = meters / self.units[to_unit]

        return result

if __name__ == '__main__':
    converter = DistanceConverter()

    result_miles_to_km = converter.convert(5.0, 'mi', 'km')
    print(result_miles_to_km)

    result_feet_to_meters = converter.convert(100.0, 'ft', 'm')
    print(result_feet_to_meters)

    result_inches_to_cm = converter.convert(12.0, 'in', 'cm')
    print(result_inches_to_cm)

    try:
        converter.convert(10.0, 'mi', 'lightyear')
    except ValueError as e:
        print(str(e))

    try:
        converter.convert(-5.0, 'km', 'm')
    except ValueError as e:
        print(str(e))