class VolumeConverter:
    def __init__(self):
        self.units = {
            "L": "L",
            "ml": "ml",
            "m3": "m3",
            "gal": "gal",
            "qt": "qt",
            "pt": "pt",
            "fl_oz": "fl_oz",
            "cup": "cup",
            "tbsp": "tbsp",
            "tsp": "tsp",
            "in3": "in3",
            "ft3": "ft3",
            "cm3": "cm3"
        }
        self.to_base = {
            "L": 1.0,
            "ml": 0.001,
            "m3": 1000.0,
            "gal": 3.785411784,
            "qt": 0.946352946,
            "pt": 0.473176473,
            "fl_oz": 0.0295735295625,
            "cup": 0.2365882365,
            "tbsp": 0.01478676478125,
            "tsp": 0.00492892159375,
            "in3": 0.016387064,
            "ft3": 28.316846592,
            "cm3": 0.001
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.to_base:
            raise ValueError(f"Unknown source unit: {from_unit}")
        if to_unit not in self.to_base:
            raise ValueError(f"Unknown target unit: {to_unit}")
        if value < 0:
            raise ValueError("Volume cannot be negative")
        base_value = value * self.to_base[from_unit]
        result = base_value / self.to_base[to_unit]
        return result

if __name__ == "__main__":
    converter = VolumeConverter()
    liters = 5
    ml = converter.convert(liters, "L", "ml")
    gallons = converter.convert(liters, "L", "gal")
    cubic_meters = converter.convert(liters, "L", "m3")
    quarts = converter.convert(liters, "L", "qt")
    cubic_inches = converter.convert(liters, "L", "in3")
    print(f"{liters} L = {ml} ml")
    print(f"{liters} L = {gallons} gal")
    print(f"{liters} L = {cubic_meters} m3")
    print(f"{liters} L = {quarts} qt")
    print(f"{liters} L = {cubic_inches} in3")
    
    sample_gallons = 10
    liters_from_gallons = converter.convert(sample_gallons, "gal", "L")
    ml_from_gallons = converter.convert(sample_gallons, "gal", "ml")
    print(f"{sample_gallons} gal = {liters_from_gallons} L")
    print(f"{sample_gallons} gal = {ml_from_gallons} ml")