class VolumeCalculator:
    def __init__(self, target_unit: str = "liters") -> None:
        self.conversion_factors = {
            "milliliters": 0.001,
            "liters": 1.0,
            "cubic_meters": 1000.0,
            "gallons": 3.78541,
            "quarts": 0.946353,
            "pints": 0.473176,
            "cups": 0.236588,
            "fluid_ounces": 0.0295735,
        }
        self.target_unit = target_unit.lower()

    def calculate_total_volume(self, volumes: list, units: list) -> float:
        if len(volumes) != len(units):
            raise ValueError("Volumes and units lists must be of the same length.")
        
        if self.target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {self.target_unit}")
        
        total_liters = sum(
            vol * self.conversion_factors.get(unit.lower(), 0)
            for vol, unit in zip(volumes, units)
        )
        
        result = total_liters / self.conversion_factors[self.target_unit]
        return result

if __name__ == '__main__':
    calculator = VolumeCalculator(target_unit="gallons")
    volumes = [500, 2, 1.5, 100]
    units = ["milliliters", "liters", "cubic_meters", "fluid_ounces"]
    total = calculator.calculate_total_volume(volumes, units)
    print(total)