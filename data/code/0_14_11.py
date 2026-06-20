def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    if from_unit_lower not in units:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit_lower not in units:
        raise ValueError(f"Invalid target unit: {to_unit}")
        
    meters = value * units[from_unit_lower]
    result = meters / units[to_unit_lower]
    return result

class LengthConverter:
    def __init__(self):
        self.units = {
            'm': 1.0,
            'km': 1000.0,
            'cm': 0.01,
            'mm': 0.001,
            'in': 0.0254,
            'ft': 0.3048,
            'yd': 0.9144,
            'mi': 1609.344
        }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()
        
        if from_unit_lower not in self.units:
            raise ValueError(f"Invalid source unit: {from_unit}")
        if to_unit_lower not in self.units:
            raise ValueError(f"Invalid target unit: {to_unit}")
            
        meters = value * self.units[from_unit_lower]
        return meters / self.units[to_unit_lower]

if __name__ == '__main__':
    sample_value = 1.0
    result1 = convert_length(sample_value, 'km', 'm')
    print(f"{sample_value} km = {result1} m")
    
    result2 = convert_length(100.0, 'cm', 'in')
    print(f"100 cm = {result2} in")
    
    result3 = convert_length(5.0, 'mi', 'km')
    print(f"5 mi = {result3} km")
    
    converter = LengthConverter()
    result4 = converter.convert(12.0, 'ft', 'm')
    print(f"12 ft = {result4} m")
    
    result5 = converter.convert(1.0, 'yd', 'ft')
    print(f"1 yd = {result5} ft")
    
    result6 = convert_length(1000.0, 'mm', 'in')
    print(f"1000 mm = {result6} in")