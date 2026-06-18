import math
class MassConverter:
    def __init__(self):
        self.s_i_base = "kg"
        self.conversion_factors = {
            "g": 0.001,                   
            "mg": 1e-6,                       
            "µg": 1e-9,                       
            "kg": 1,                          
            "t": 1000,                    
            "lb": 0.45359237,               
            "oz": 0.02834952,               
        }
    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported unit '{from_unit}' or '{to_unit}'. Supported units are {list(self.conversion_factors.keys())}")
        factor_from_si = self.conversion_factors[from_unit]
        factor_to_si = self.conversion_factors[to_unit]
        value_in_si = value * factor_from_si
        result_value = value_in_si / factor_to_si
        return round(result_value, 6)
if __name__ == '__main__':
    converter = MassConverter()
    test_cases = [
        (100, "g", "kg"),                               
        (5000, "mg", "t"),                               
        (2.20462, "lb", "kg"),                          
        (35.274, "oz", "g"),                        
    ]
    for value, from_u, to_u in test_cases:
        result = converter.convert(value, from_u, to_u)
        print(f"{value} {from_u} is equal to {result} {to_u}")