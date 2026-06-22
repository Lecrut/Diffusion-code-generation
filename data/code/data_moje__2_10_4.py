class VolumeCalculator:
    UNIT_CONVERSIONS = {
        'ml': 1.0,
        'liter': 1000.0,
        'gallon': 3785.41,
        'cup': 236.588,
        'pint': 473.176,
        'quart': 946.353,
        'cubic_meter': 1000000.0,
        'cubic_centimeter': 1.0,
    }

    def calculate_total_volume(self, measurements: list[dict], target_unit: str) -> float:
        target_unit_lower = target_unit.lower()
        if target_unit_lower not in self.UNIT_CONVERSIONS:
            raise ValueError(f"Unsupported target unit: {target_unit}")

        target_factor = self.UNIT_CONVERSIONS[target_unit_lower]
        total_in_ml = sum(
            self._convert_to_ml(item['value'], item['unit'])
            for item in measurements
        )
        return total_in_ml / target_factor

    def _convert_to_ml(self, value: float, unit: str) -> float:
        unit_lower = unit.lower()
        if unit_lower not in self.UNIT_CONVERSIONS:
            raise ValueError(f"Unsupported unit: {unit}")
        factor = self.UNIT_CONVERSIONS[unit_lower]
        return value * factor

if __name__ == '__main__':
    calculator = VolumeCalculator()
    sample_measurements = [
        {'value': 1.5, 'unit': 'gallon'},
        {'value': 500, 'unit': 'ml'},
        {'value': 2, 'unit': 'liter'},
        {'value': 3, 'unit': 'cup'},
    ]
    result = calculator.calculate_total_volume(sample_measurements, 'liter')
    print(result)