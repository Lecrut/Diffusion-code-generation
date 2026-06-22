class VolumeCalculator:
    def __init__(self):
        self.conversion_factors = {
            "liters": 1.0,
            "milliliters": 0.001,
            "gallons": 3.78541,
            "cubic_meters": 1000.0,
            "cubic_centimeters": 0.001,
            "fluid_ounces": 0.0295735,
            "pints": 0.473176,
            "quarts": 0.946353,
            "cups": 0.236588,
        }

    def calculate_total_volume(self, volumes: list[tuple[float, str]], target_unit: str) -> float:
        total_liters = sum(volume * self.conversion_factors[unit] for volume, unit in volumes)
        total_target = total_liters / self.conversion_factors[target_unit]
        return round(total_target, 6)

if __name__ == '__main__':
    calculator = VolumeCalculator()
    measurements = [
        (1000, "milliliters"),
        (1.5, "liters"),
        (2, "gallons"),
        (0.5, "cubic_meters"),
    ]
    result = calculator.calculate_total_volume(measurements, "liters")
    print(result)