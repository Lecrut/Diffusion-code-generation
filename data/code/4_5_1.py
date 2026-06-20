class DistanceConverter:
    SUPPORTED_UNITS = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.344,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }

    def __init__(self):
        self.valid_units = set(self.SUPPORTED_UNITS.keys())

    def convert(self, value, from_unit, to_unit):
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()

        if from_unit_lower not in self.valid_units:
            raise ValueError(f"Source unit '{from_unit}' is not supported.")
        if to_unit_lower not in self.valid_units:
            raise ValueError(f"Target unit '{to_unit}' is not supported.")
        
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Distance value must be a non-negative number.")

        value_in_meters = value * self.SUPPORTED_UNITS[from_unit_lower]
        result = value_in_meters / self.SUPPORTED_UNITS[to_unit_lower]
        return result

if __name__ == '__main__':
    converter = DistanceConverter()
    result = converter.convert(5, 'mile', 'kilometer')
    print(result)
    result_meters = converter.convert(100, 'meter', 'foot')
    print(result_meters)