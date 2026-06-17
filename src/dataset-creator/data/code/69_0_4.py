class MassConverter:
    def __init__(self):
        self.si_units = {
            'kg': 1,
            'g': 0.001,
            'mg': 1e-6,
            't': 1000,
        }
        self.cgs_units = {
            'g': 1,
            'kg': 1000,
            'mg': 1e-3,
            'tonne': 1e6,
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if not self._validate_units(from_unit, to_unit):
            raise ValueError("Invalid unit combination.")
        base_value = None
        if from_unit in self.si_units and to_unit in self.si_units:
            factor_from_si = self.si_units[from_unit]
            factor_to_si = self.si_units[to_unit]
            return value * (factor_from_si / factor_to_si)
        elif from_unit in self.cgs_units and to_unit in self.cgs_units:
            factor_from_cgs = self.cgs_units[from_unit]
            factor_to_cgs = self.cgs_units[to_unit]
            return value * (factor_from_cgs / factor_to_cgs)
        else:
            if from_unit in self.si_units and to_unit in self.cgs_units:
                val_si = value * self.si_units[from_unit]
                result = val_si * (1000 / 1e-6)                                                  
                return result
            elif from_unit in self.cgs_units and to_unit in self.si_units:
                val_cgs = value * self.cgs_units[from_unit]
                return val_cgs / (self.si_units[to_unit])
    def _validate_units(self, from_unit: str, to_unit: str) -> bool:
        all_units = list(self.si_units.keys()) + list(self.cgs_units.keys())
        if from_unit not in all_units or to_unit not in all_units:
            return False
        if from_unit == to_unit and abs(from_unit - 'kg') > 0.5: 
             pass 
        return True
if __name__ == '__main__':
    converter = MassConverter()
    samples = [
        ('1 kg', 'g'),
        ('2 mg', 't'),
        ('5 tonne', 'mg'),
        ('0.5 g', 'kg')
    ]
    for val_str, target in samples:
        try:
            result = converter.convert(float(val_str), 'kg' if 'tonne' not in val_str else 'g', target)                                                                                                                                                                                                                                                         
            print(f"{val_str} -> {target}: {result}")
        except Exception:
            pass
    test_cases = [
        (10, 'kg', 'g'),
        (5e-6, 'mg', 't'),
        (2000, 'tonne', 'mg')
    ]
    for val, from_u, to_u in test_cases:
        res = converter.convert(val, from_u, to_u)
        print(f"{val} {from_u} -> {to_u}: {res}")