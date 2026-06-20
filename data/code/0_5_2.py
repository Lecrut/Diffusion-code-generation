class UnitConverter:
    def __init__(self, base_unit, factors):
        self.base_unit = base_unit
        self.factors = factors
        if base_unit not in factors:
            raise KeyError(f"Base unit '{base_unit}' not in conversion factors.")

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors:
            raise KeyError(f"Unknown unit: {from_unit}")
        if to_unit not in self.factors:
            raise KeyError(f"Unknown unit: {to_unit}")
        
        value_in_base = value * self.factors[from_unit]
        result = value_in_base / self.factors[to_unit]
        return result

if __name__ == '__main__':
    factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'feet': 0.3048
    }

    converter = UnitConverter('meters', factors)

    km_to_m = converter.convert(1.0, 'kilometers', 'meters')
    miles_to_cm = converter.convert(1.0, 'miles', 'centimeters')
    feet_to_km = converter.convert(1.0, 'feet', 'kilometers')

    print(km_to_m)
    print(miles_to_cm)
    print(feet_to_km)