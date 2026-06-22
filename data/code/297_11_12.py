class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            "gallons": 3.78541,
            "liters": 1.0
        }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError("Invalid unit provided")
        if from_unit == to_unit:
            return round(value, 2)
        base_value = value * self.conversion_factors[from_unit]
        result = round(base_value / self.conversion_factors[to_unit], 2)
        return result

if __name__ == '__main__':
    converter = UnitConverter()
    print(f"10 gallons to liters: {converter.convert(10.0, 'gallons', 'liters')}")
    print(f"5 liters to gallons: {converter.convert(5.0, 'liters', 'gallons')}")
    print(f"20 gallons to liters: {converter.convert(20.0, 'gallons', 'liters')}")