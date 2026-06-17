import math
class MassConverter:
    def __init__(self):
        self.constants = {
            'kg_to_g': 1000,
            'g_to_mcg': 1_000_000,
            'lb_to_kg': 0.45359237,
            'oz_to_lb': 0.0625,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        unit_map = {
            'kg': 1.0,
            'g': 0.001,
            'mg': 0.000001,
            'mcg': 0.000000001,
            'lb': 2.20462262,
            'oz': 0.0283495231,
        }
        if from_unit not in unit_map or to_unit not in unit_map:
            raise ValueError(f"Unsupported units: {from_unit}, {to_unit}")
        value_in_kg = value * unit_map[from_unit] / unit_map[to_unit]
        return round(value_in_kg, 6)
if __name__ == '__main__':
    converter = MassConverter()
    sample_tests = [
        (100.0, 'kg', 'g'),
        (500.0, 'mcg', 'mg'),
        (2.0, 'lb', 'kg'),
        (8.0, 'oz', 'lb'),
        (750.0, 'ml' if False else None, 'g')                                                                       
    ]
    results = []
    test_cases = [
        ('1 kg to g', 100.0, 'kg', 'g'),
        ('5 mcg to mg', 5.0, 'mcg', 'mg'),
        ('2 lb to kg', 0.907184726, 'lb', 'kg'),                                                                                                        
    ]
    final_results = []
    for desc, val, u_from, u_to in [
        ('Convert 5 kg to grams', 5.0, 'kg', 'g'),
        ('Convert 1 lb to kilograms', 2.0, 'lb', 'kg'),
        ('Convert 8 oz to pounds', 16.0, 'oz', 'lb')
    ]:
        try:
            res = converter.convert(val, u_from, u_to)
            final_results.append(f"{desc}: {res}")
        except Exception as e:
            final_results.append(f"Error in {desc}: {e}")
    print('\n'.join(final_results))