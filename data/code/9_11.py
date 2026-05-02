class VolumeConverter:
    def __init__(self):
        self.base_unit = "liters"
        self.conversion_factors = {
            "liters": 1.0,
            "ml": 0.001,
            "cubic_meters": 1000.0,
            "cubic_feet": 28.316847,
            "gallons": 3.78541,
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
    volume_ml = 500.0
    volume_m3 = 0.5
    volume_gallons = 10.0
    volume_liters = 20.0
    print(f"Converting {volume_ml} ml to liters: {converter.to_base(volume_ml, 'ml'):.4f} L")
    print(f"Converting {volume_m3} cubic_meters to liters: {converter.to_base(volume_m3, 'cubic_meters'):.4f} L")
    print(f"Converting {volume_gallons} gallons to liters: {converter.to_base(volume_gallons, 'gallons'):.4f} L")
    print(f"Converting {volume_liters} liters to liters: {converter.to_base(volume_liters, 'liters'):.4f} L")
    print("\nTesting conversion from base unit (liters) to other units:")
    result_ml = converter.from_base(10.0, 'liters')
    print(f"Converting 10.0 liters to ml: {result_ml * converter.conversion_factors['ml']:.2f} ml")
    result_m3 = converter.from_base(5.0, 'liters')
    print(f"Converting 5.0 liters to cubic_meters: {result_m3 / converter.conversion_factors['cubic_meters']:.4f} m^3")
    result_gallons = converter.from_base(10.0, 'liters')
    print(f"Converting 10.0 liters to gallons: {result_gallons / converter.conversion_factors['gallons']:.4f} gal")
    try:
        converter.to_base(10.0, 'furlongs')
    except ValueError as e:
        print(f"\nError caught as expected: {e}")