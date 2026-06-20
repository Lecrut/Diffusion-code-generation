class DistanceConverter:
    def __init__(self):
        self._units_to_meters = {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'mile': 1609.344,
            'yard': 0.9144,
            'foot': 0.3048,
            'inch': 0.0254,
        }

    def _normalize_unit(self, unit):
        return unit.lower().strip()

    def _validate_unit(self, unit):
        normalized = self._normalize_unit(unit)
        if normalized not in self._units_to_meters:
            raise ValueError(f"Unsupported unit: '{unit}'. Supported units: {list(self._units_to_meters.keys())}")
        return normalized

    def convert(self, value, from_unit, to_unit):
        if value < 0:
            raise ValueError("Distance cannot be negative.")
        
        from_norm = self._validate_unit(from_unit)
        to_norm = self._validate_unit(to_unit)
        
        if value == 0:
            return 0.0
        
        factor_from = self._units_to_meters[from_norm]
        factor_to = self._units_to_meters[to_norm]
        
        value_in_meters = value * factor_from
        converted_value = value_in_meters / factor_to
        
        return converted_value

if __name__ == '__main__':
    converter = DistanceConverter()
    
    result1 = converter.convert(1, 'kilometer', 'mile')
    print(result1)
    
    result2 = converter.convert(1, 'mile', 'kilometer')
    print(result2)
    
    result3 = converter.convert(100, 'centimeter', 'inch')
    print(result3)
    
    result4 = converter.convert(5.28, 'foot', 'meter')
    print(result4)