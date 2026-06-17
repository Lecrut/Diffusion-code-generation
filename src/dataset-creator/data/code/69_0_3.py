import math
class MassConverter:
    def __init__(self):
        self.si_base = "kg"
        self.cgs_base = "g"
        self.si_factors = {
            "mg": 1e-6,
            "ug": 1e-9,
            "ng": 1e-12,
            "kg": 1.0,
            "g": 1e-3,
        }
        self.cgs_factors = {
            "mg": 1e-3,
            "ug": 1e-6,
            "ng": 1e-9,
            "g": 1.0,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        unit_lower = from_unit.lower()
        target_lower = to_unit.lower()
        if not self._is_valid_unit(unit_lower):
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if not self._is_valid_unit(target_lower):
            raise ValueError(f"Unsupported target unit: {to_unit}")
        value_in_base = 0.0
        is_si_source = any(unit in self.si_factors for unit in [unit_lower])
        if is_si_source:
            factor_from_base = self.si_factors[unit_lower]
            value_in_base = value * factor_from_base
            is_si_target = any(u in self.si_factors for u in [target_lower])
            if not is_si_target:
                raise ValueError(f"Target unit {to_unit} must be an SI unit")
        else:
            factor_from_base = self.cgs_factors[unit_lower]
            value_in_base = value * (factor_from_base / 1000.0)                    
            is_si_target = any(u in self.si_factors for u in [target_lower])
            if not is_si_target:
                raise ValueError(f"Target unit {to_unit} must be an SI unit")
        factor_to_base = self.si_factors[target_lower]
        return value_in_base / factor_to_base
    def _is_valid_unit(self, unit):
        valid_si_units = set(self.si_factors.keys()) | {"kg", "g"}                                    
        valid_cgs_units = set(self.cgs_factors.keys()) | {"g"}                                    
        return (unit in self.si_factors) or unit == 'kg'
if __name__ == '__main__':
    converter = MassConverter()
    test_cases = [
        ("100", "mg", "kg"),
        ("5.2", "g", "kg"),
        ("3400", "mg", "g"),
        ("7e-6", "ug", "ng"),
        ("800", "g", "kg")
    ]
    for value_str, from_u, to_u in test_cases:
        try:
            result = converter.convert(float(value_str), from_u, to_u)
            print(f"{value_str} {from_u} -> {result:.6f} {to_u}")
        except ValueError as e:
            print(f"Error converting {value_str} {from_u} to {to_u}: {e}")