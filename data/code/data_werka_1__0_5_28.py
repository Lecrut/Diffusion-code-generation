class UnitConverter:
    def __init__(self, base_unit, factors):
        self.base_unit = base_unit
        self.factors = {k: v for k, v in factors.items()}

    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.factors or to_unit not in self.factors:
            raise ValueError(f"Unit not supported: {from_unit} or {to_unit}")
        
        base_value = value * self.factors[from_unit]
        result = base_value / self.factors[to_unit]
        return result

def main():
    factors = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'mi': 1609.344
    }
    
    converter = UnitConverter('m', factors)
    
    val = 5.0
    from_u = 'km'
    to_u = 'mi'
    
    result = converter.convert(val, from_u, to_u)
    print(f"{val} {from_u} is {result} {to_u}")

if __name__ == '__main__':
    main()