class VolumeCalculator:
    UNIT_CONVERSIONS = {
        'liters': 1.0,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'cubic_meters': 1000.0,
        'cubic_feet': 28.3168,
        'cubic_inches': 0.0163871,
        'pints': 0.473176,
        'quarts': 0.946353,
        'cups': 0.236588
    }

    def __init__(self, measurements: list[float], unit: str):
        if unit not in self.UNIT_CONVERSIONS:
            raise ValueError(f"Unsupported unit: {unit}")
        self.measurements = measurements
        self.unit = unit

    def get_total_volume(self, target_unit: str) -> float:
        if target_unit not in self.UNIT_CONVERSIONS:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        conversion_factor_to_base = self.UNIT_CONVERSIONS[self.unit]
        conversion_factor_to_target = self.UNIT_CONVERSIONS[target_unit]
        
        total_in_base_units = sum(
            measurement * conversion_factor_to_base
            for measurement in self.measurements
        )
        
        total_in_target_units = total_in_base_units / conversion_factor_to_target
        return total_in_target_units

if __name__ == '__main__':
    measurements = [1000.0, 500.0, 250.0]
    calculator = VolumeCalculator(measurements, 'milliliters')
    result = calculator.get_total_volume('liters')
    print(result)