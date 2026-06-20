class DistanceConverter:
    def __init__(self):
        self.units = {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'mile': 1609.344,
            'yard': 0.9144,
            'foot': 0.3048,
            'inch': 0.0254
        }

    def convert(self, value, from_unit, to_unit):
        from_unit_lower = from_unit.lower().strip()
        to_unit_lower = to_unit.lower().strip()
        
        if from_unit_lower not in self.units:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit_lower not in self.units:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        if value < 0:
            raise ValueError("Distance value cannot be negative")
        
        base_value = value * self.units[from_unit_lower]
        result = base_value / self.units[to_unit_lower]
        
        return result

if __name__ == '__main__':
    converter = DistanceConverter()
    
    sample_distance = 5.0
    source_unit = 'kilometer'
    target_unit = 'mile'
    
    result = converter.convert(sample_distance, source_unit, target_unit)
    print(result)
    
    another_result = converter.convert(1.0, 'foot', 'meter')
    print(another_result)