class DistanceConverter:
    UNIT_CONVERSIONS = {
        'meter': 1.0,
        'm': 1.0,
        'kilometer': 1000.0,
        'km': 1000.0,
        'mile': 1609.344,
        'mi': 1609.344,
        'foot': 0.3048,
        'ft': 0.3048,
        'inch': 0.0254,
        'in': 0.0254,
        'centimeter': 0.01,
        'cm': 0.01,
        'millimeter': 0.001,
        'mm': 0.001,
        'yard': 0.9144,
        'yd': 0.9144,
        'nautical_mile': 1852.0,
        'nm': 1852.0,
    }

    def __init__(self):
        self.supported_units = list(self.UNIT_CONVERSIONS.keys())

    def convert(self, distance, from_unit, to_unit):
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()

        if from_unit_lower not in self.supported_units:
            raise ValueError(f"Unsupported source unit: {from_unit}. Supported units: {', '.join(self.supported_units)}")
        if to_unit_lower not in self.supported_units:
            raise ValueError(f"Unsupported target unit: {to_unit}. Supported units: {', '.join(self.supported_units)}")

        if not isinstance(distance, (int, float)):
            raise TypeError("Distance must be a number")

        if distance < 0:
            raise ValueError("Distance cannot be negative")

        meters = distance * self.UNIT_CONVERSIONS[from_unit_lower]
        result = meters / self.UNIT_CONVERSIONS[to_unit_lower]

        return result

def main():
    converter = DistanceConverter()

    sample_cases = [
        (1, 'kilometer', 'mile'),
        (5280, 'foot', 'meter'),
        (100, 'meter', 'foot'),
        (1, 'mile', 'kilometer'),
        (3, 'yard', 'meter'),
        (10, 'inch', 'centimeter'),
        (5, 'nautical_mile', 'kilometer'),
    ]

    for distance, from_unit, to_unit in sample_cases:
        try:
            result = converter.convert(distance, from_unit, to_unit)
            print(f"{distance} {from_unit} = {result:.6f} {to_unit}")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")

    error_cases = [
        (10, 'lightyear', 'meter'),
        (-5, 'meter', 'kilometer'),
        ('abc', 'meter', 'kilometer'),
    ]

    for distance, from_unit, to_unit in error_cases:
        try:
            result = converter.convert(distance, from_unit, to_unit)
            print(f"{distance} {from_unit} = {result:.6f} {to_unit}")
        except (ValueError, TypeError) as e:
            print(f"Error converting {distance} {from_unit} to {to_unit}: {e}")

if __name__ == '__main__':
    main()