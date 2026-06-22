UNIT_RATIOS = {
    'meter': 1.0,
    'm': 1.0,
    'kilometer': 1000.0,
    'km': 1000.0,
    'mile': 1609.344,
    'mi': 1609.344,
    'foot': 0.3048,
    'ft': 0.3048,
    'inch': 0.0254,
    'in': 0.0254,
    'centimeter': 0.01,
    'cm': 0.01,
    'millimeter': 0.001,
    'mm': 0.001,
    'yard': 0.9144,
    'yd': 0.9144,
}

class DistanceSystem:
    def __init__(self):
        self.ratios = UNIT_RATIOS

    def validate_unit(self, unit):
        normalized = unit.lower().strip()
        if normalized not in self.ratios:
            raise ValueError(f"Unit '{unit}' is not supported")
        return normalized

    def convert(self, value, source, target):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        
        src_norm = self.validate_unit(source)
        tgt_norm = self.validate_unit(target)
        
        meters = value * self.ratios[src_norm]
        result = meters / self.ratios[tgt_norm]
        
        return result

if __name__ == '__main__':
    system = DistanceSystem()
    
    result_1 = system.convert(100, 'meter', 'foot')
    print(result_1)
    
    result_2 = system.convert(1, 'mile', 'km')
    print(result_2)
    
    result_3 = system.convert(5, 'km', 'meter')
    print(result_3)
    
    result_4 = system.convert(72, 'inch', 'centimeter')
    print(result_4)
    
    try:
        system.convert(10, 'meter', 'lightyear')
    except ValueError as e:
        print(e)