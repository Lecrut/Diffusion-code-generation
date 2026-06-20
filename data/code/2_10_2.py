class VolumeCalculator:
    CONVERSIONS_TO_LITER = {
        "liter": 1.0,
        "milliliter": 0.001,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "cup": 0.236588,
        "fluid_ounce": 0.0295735,
        "tablespoon": 0.0147868,
        "teaspoon": 0.00492892,
        "cubic_meter": 1000.0,
        "cubic_centimeter": 0.001,
        "cubic_inch": 0.0163871,
        "cubic_foot": 28.3168,
    }

    def calculate_total(self, measurements: list, target_unit: str) -> float:
        target_unit_lower = target_unit.lower()
        if target_unit_lower not in self.CONVERSIONS_TO_LITER:
            raise ValueError(f"Unsupported target unit: {target_unit}")

        total_in_liters = sum(
            value * self.CONVERSIONS_TO_LITER[unit.lower()]
            for value, unit in measurements
        )

        return total_in_liters / self.CONVERSIONS_TO_LITER[target_unit_lower]

if __name__ == '__main__':
    calculator = VolumeCalculator()
    measurements = [
        (1.0, "gallon"),
        (500.0, "milliliter"),
        (2.0, "liter"),
        (16.0, "fluid_ounce"),
    ]
    total_liters = calculator.calculate_total(measurements, "liter")
    print(total_liters)
    total_gallons = calculator.calculate_total(measurements, "gallon")
    print(total_gallons)
    total_ml = calculator.calculate_total(measurements, "milliliter")
    print(total_ml)