import math
class MassConverter:
    def __init__(self):
        self.s_i_base = "kg"                            
        self.factors_si = {
            "kg": 1,
            "g": 0.001,
            "mg": 1e-6,
            "µg": 1e-9,
            "tonne": 1000,
            "lb": 0.45359237,
            "oz": 0.028349523125,
        }
        self.factors_cgs = {
            "g": 1000,
            "mg": 1e6,
            "µg": 1e9,
            "kg": 1/1000,                                                                                                                                      
            "tonne": 1/1000,
        }
    def convert(self, mass_value: float, from_unit: str, to_unit: str) -> float:
        if mass_value < 0:
            raise ValueError("Mass cannot be negative.")
        u_from = from_unit.lower().strip()
        u_to = to_unit.lower().strip()
        if u_from not in self.factors_si or u_to not in self.factors_cgs:
            raise ValueError(f"Unsupported unit '{u_from}' -> '{u_to}'. Supported units are keys of factors.")
        value_in_kg = mass_value * self.factors_si[u_from]
        value_in_target = value_in_kg * self.factors_cgs[u_to]
        return value_in_target
if __name__ == '__main__':
    converter = MassConverter()
    test_cases = [
        ("1", "kg", "g"),                              
        ("5.2876", "lb", "oz"),                           
        ("1e-3", "mg", "µg"),                           
        ("1000", "tonne", "kg"),                              
        ("275.4689", "oz", "lb"),                                     
    ]
    for val, src, dst in test_cases:
        try:
            result = converter.convert(float(val), src, dst)
            print(f"Converted {val} {src} to {dst}: {result}")
        except ValueError as e:
            print(f"Error converting {val} from {src} to {dst}: {e}")
    try:
        res = converter.convert(1.5, "kg", "tonne")
        print(f"Converted 1.5 kg to tonne: {res}")
    except Exception as e:
        print(e)