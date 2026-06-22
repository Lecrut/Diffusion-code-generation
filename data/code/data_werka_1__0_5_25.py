class UnitConverter:
    def __init__(self, base_unit, factors):
        self.base_unit = base_unit
        self.factors = factors

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors or to_unit not in self.factors:
            raise ValueError(f"Unknown unit: {from_unit} or {to_unit}")
        
        base_value = value * self.factors[from_unit]
        result = base_value / self.factors[to_unit]
        return result

def run_conversion():
    factors = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.344
    }

    converter = UnitConverter('meter', factors)

    val_m_to_km = converter.convert(5280, 'foot', 'kilometer')
    val_km_to_cm = converter.convert(1.5, 'kilometer', 'centimeter')
    val_in_to_mm = converter.convert(10, 'inch', 'millimeter')
    val_mi_to_m = converter.convert(1, 'mile', 'meter')

    print(val_m_to_km)
    print(val_km_to_cm)
    print(val_in_to_mm)
    print(val_mi_to_m)

if __name__ == '__main__':
    run_conversion()