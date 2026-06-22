class VolumeConverter:
    _UNITS_LITERS = {
        "liter": 1.0,
        "milliliter": 0.001,
        "gallon": 3.785411784,
        "quart": 0.946352946,
        "pint": 0.473176473,
        "cup": 0.2365882365,
        "fluid_ounce": 0.0295735295625
    }

    _VALID_KEYS = frozenset(_UNITS_LITERS.keys())

    def __init__(self):
        self._conversion_cache = {}

    def _normalize_unit(self, unit):
        u = unit.lower().strip()
        if u in self._VALID_KEYS:
            return u
        raise ValueError(f"Unknown unit: {unit}")

    def convert(self, value, from_unit, to_unit):
        from_key = self._normalize_unit(from_unit)
        to_key = self._normalize_unit(to_unit)
        
        if from_key == to_key:
            return value
        
        cache_key = (from_key, to_key)
        if cache_key in self._conversion_cache:
            factor = self._conversion_cache[cache_key]
        else:
            factor = self._UNITS_LITERS[from_key] / self._UNITS_LITERS[to_key]
            self._conversion_cache[cache_key] = factor
            
        return value * factor

    def convert_batch(self, values, from_unit, to_unit):
        factor = 0.0
        from_key = self._normalize_unit(from_unit)
        to_key = self._normalize_unit(to_unit)
        
        if from_key != to_key:
            cache_key = (from_key, to_key)
            if cache_key in self._conversion_cache:
                factor = self._conversion_cache[cache_key]
            else:
                factor = self._UNITS_LITERS[from_key] / self._UNITS_LITERS[to_key]
                self._conversion_cache[cache_key] = factor
        else:
            factor = 1.0
            
        return [v * factor for v in values]

if __name__ == '__main__':
    converter = VolumeConverter()
    
    result1 = converter.convert(1, "gallon", "liter")
    print(f"1 gallon to liter: {result1}")
    
    result2 = converter.convert(3.785411784, "liter", "gallon")
    print(f"3.785411784 liter to gallon: {result2}")
    
    result3 = converter.convert(16, "fluid_ounce", "cup")
    print(f"16 fluid_ounce to cup: {result3}")
    
    result4 = converter.convert(1000, "milliliter", "liter")
    print(f"1000 milliliter to liter: {result4}")
    
    batch_values = [1, 2, 5, 10]
    batch_result = converter.convert_batch(batch_values, "quart", "liter")
    print(f"Batch conversion of {batch_values} quarts to liters: {batch_result}")
    
    try:
        converter.convert(1, "invalid_unit", "liter")
    except ValueError as e:
        print(f"Error caught: {e}")