class VolumeConverter:
    def __init__(self):
        self.base_unit = "liters"
        self.conversion_factors = {
            "liters": 1.0,
            "ml": 0.001,
            "us_gal": 3.78541,
            "gallons": 3.78541,
            "cubic_meters": 1000.0,
            "m3": 1000.0
        }
    def to_base(self, volume: float, unit: str) -> float:
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        if unit == self.base_unit:
            return volume
        return volume * self.conversion_factors[unit]
    def from_base(self, volume_base: float, unit: str) -> float:
        if unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit: {unit}")
        if unit == self.base_unit:
            return volume_base
        return volume_base / self.conversion_factors[unit]
if __name__ == '__main__':
    converter = VolumeConverter()
    print("--- Conversion Tests ---")
    volume_liters = 5.0
    print(f"\nConverting {volume_liters} liters:")
    print(f"To ml: {converter.to_base(volume_liters, 'liters')}")
    print(f"To us_gal: {converter.from_base(volume_liters, 'us_gal')}")
    print(f"To m3: {converter.from_base(volume_liters, 'm3')}")
    volume_us_gal = 10.0
    print(f"\nConverting {volume_us_gal} US gallons:")
    print(f"To liters: {converter.to_base(volume_us_gal, 'us_gal')}")
    volume_m3 = 2.5
    print(f"\nConverting {volume_m3} cubic meters:")
    print(f"To liters: {converter.to_base(volume_m3, 'm3')}")
    volume_input = 100.0
    unit_input = "gallons"
    print(f"\nConverting {volume_input} {unit_input} to liters and back:")
    liters = converter.to_base(volume_input, unit_input)
    result_liters = converter.from_base(liters, "liters")
    print(f"Result: {result_liters} liters")