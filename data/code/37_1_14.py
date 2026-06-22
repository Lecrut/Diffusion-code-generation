class GeometryCalculator:
    _units = {
        "cm": 1,
        "m": 100,
        "km": 100000,
        "in": 2.54,
        "ft": 30.48,
        "yd": 91.44
    }

    @staticmethod
    def calculate_parallelogram_area(base, height, unit="cm"):
        if unit not in GeometryCalculator._units:
            raise ValueError(f"Unsupported unit: {unit}")
        return base * height

    @staticmethod
    def get_area_in_standard_units(base, height, input_unit, output_unit="cm"):
        if input_unit not in GeometryCalculator._units:
            raise ValueError(f"Unsupported input unit: {input_unit}")
        if output_unit not in GeometryCalculator._units:
            raise ValueError(f"Unsupported output unit: {output_unit}")
        base_in_cm = base * GeometryCalculator._units[input_unit]
        height_in_cm = height * GeometryCalculator._units[input_unit]
        area_cm = base_in_cm * height_in_cm
        return area_cm / GeometryCalculator._units[output_unit]

if __name__ == '__main__':
    base_value = 12
    height_value = 7
    result = GeometryCalculator.calculate_parallelogram_area(base_value, height_value)
    print(result)