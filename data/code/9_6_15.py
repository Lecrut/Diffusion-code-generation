class VolumeConverter:
    def __init__(self):
        base_unit = "liters"
        self.conversion_factors = {
            "ml": 0.001,
            "l": 1.0,
            "gal": 3.78541,
            "m3": 1000.0,
            "ft3": 28.3168,
            "cup": 0.236588,
            "pt": 0.473176,
            "qt": 0.946353,
            "tbsp": 0.0147868,
            "tsp": 0.00492892
        }
        self.base_unit = base_unit

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {to_unit}")

        value_in_base = value / self.conversion_factors[from_unit]
        result = value_in_base * self.conversion_factors[to_unit]
        return result

if __name__ == '__main__':
    converter = VolumeConverter()
    liters_to_ml = converter.convert(1, "l", "ml")
    cubic_meters_to_gallons = converter.convert(1, "m3", "gal")
    gallons_to_liters = converter.convert(5, "gal", "l")
    cups_to_ml = converter.convert(2, "cup", "ml")
    print(liters_to_ml)
    print(cubic_meters_to_gallons)
    print(gallons_to_liters)
    print(cups_to_ml)