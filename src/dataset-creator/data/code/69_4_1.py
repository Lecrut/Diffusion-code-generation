from dataclasses import dataclass
@dataclass(frozen=True)
class MassUnit:
    value: float
    unit: str
    def to_kg(self):
        conversion_factors = {
            'kg': 1,
            'lb': 0.45359237,
            'oz': 0.028349523125,
            'tonne': 1000,
            'g': 0.001
        }
        if self.unit not in conversion_factors:
            raise ValueError(f"Unsupported unit: {self.unit}")
        return self.value * conversion_factors[self.unit]
@dataclass(frozen=True)
class ConversionEngine:
    source_unit: str
    def convert(self, mass_value: float, target_unit: str = 'kg') -> MassUnit:
        if not isinstance(mass_value, (int, float)):
            raise TypeError("Mass value must be a number")
        try:
            kg_value = self._convert_to_base(mass_value)
        except ValueError as e:
            return MassUnit(0.0, target_unit)
        if not isinstance(kg_value, (int, float)):
            raise TypeError("Conversion failed to produce a number")
        try:
            final_kg = self._convert_to_base(kg_value, 'kg')
        except ValueError as e:
            return MassUnit(0.0, target_unit)
        if not isinstance(final_kg, (int, float)):
            raise TypeError("Conversion failed to produce a number")
        try:
            final_mass = self._convert_to_target(target_unit, final_kg)
        except ValueError as e:
            return MassUnit(0.0, target_unit)
        if not isinstance(final_mass, (int, float)):
            raise TypeError("Conversion failed to produce a number")
        return MassUnit(float(final_mass), target_unit)
    def _convert_to_base(self, mass_value: float, base_unit: str = 'kg') -> float:
        conversion_factors = {
            'kg': 1.0,
            'lb': 2.20462262,
            'oz': 35.27396195,
            'tonne': 0.001,
            'g': 1000.0
        }
        if base_unit not in conversion_factors:
            raise ValueError(f"Unsupported unit for calculation: {base_unit}")
        return mass_value * conversion_factors[base_unit]
    def _convert_to_target(self, target_unit: str, value_in_kg: float) -> float:
        reverse_conversion_factors = {
            'kg': 1.0,
            'lb': 0.45359237,
            'oz': 0.028349523125,
            'tonne': 1000.0,
            'g': 0.001
        }
        if target_unit not in reverse_conversion_factors:
            raise ValueError(f"Unsupported unit for calculation: {target_unit}")
        return value_in_kg * reverse_conversion_factors[target_unit]
if __name__ == '__main__':
    engine = ConversionEngine(source_unit='lb')
    test_cases = [
        (10.5, 'kg'),
        (-5.0, 'oz'),
        (0.0, 'tonne'),
        ('invalid', 'g'),                                                                                                                                                             
    ]
    results = []
    for mass_val, target_unit in test_cases:
        try:
            result = engine.convert(mass_val, target_unit)
            results.append(result)
        except Exception as e:
            results.append(MassUnit(0.0, 'kg'))
    for i, res in enumerate(results):
        print(f"Test Case {i+1}: Input={test_cases[i][0]}, Target={test_cases[i][1]} -> Result: {res.value} {res.unit}")