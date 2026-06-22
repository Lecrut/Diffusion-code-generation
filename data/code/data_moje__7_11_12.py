from fractions import Fraction
from decimal import Decimal, getcontext

getcontext().prec = 50

class TimeConverter:
    UNITS = {
        'second': 1,
        'minute': 60,
        'hour': 3600,
        'day': 86400,
        'week': 604800,
        'month': 2629746,
        'year': 31556952
    }

    def __init__(self):
        self._cache = {}

    def _get_factor(self, unit):
        unit_lower = unit.lower()
        if unit_lower in self.UNITS:
            return Fraction(self.UNITS[unit_lower])
        raise ValueError(f"Unknown unit: {unit}")

    def convert(self, value, from_unit, to_unit):
        from_factor = self._get_factor(from_unit)
        to_factor = self._get_factor(to_unit)
        
        value_in_seconds = Fraction(value) * from_factor
        result = value_in_seconds / to_factor
        
        cache_key = (value, from_unit.lower(), to_unit.lower())
        self._cache[cache_key] = result
        
        return float(result)

    def convert_precise(self, value, from_unit, to_unit):
        from_factor = self._get_factor(from_unit)
        to_factor = self._get_factor(to_unit)
        
        value_in_seconds = Decimal(value) * Decimal(from_factor)
        result = value_in_seconds / Decimal(to_factor)
        
        return float(result)

    def get_supported_units(self):
        return list(self.UNITS.keys())

    def clear_cache(self):
        self._cache.clear()

if __name__ == '__main__':
    converter = TimeConverter()
    
    seconds_to_minutes = converter.convert(3600, 'second', 'minute')
    print(seconds_to_minutes)
    
    hours_to_days = converter.convert(48, 'hour', 'day')
    print(hours_to_days)
    
    days_to_hours = converter.convert(1, 'day', 'hour')
    print(days_to_hours)
    
    weeks_to_seconds = converter.convert(1, 'week', 'second')
    print(weeks_to_seconds)
    
    precise_years_to_days = converter.convert_precise(1, 'year', 'day')
    print(precise_years_to_days)
    
    precise_minutes_to_hours = converter.convert_precise(90, 'minute', 'hour')
    print(precise_minutes_to_hours)
    
    supported = converter.get_supported_units()
    print(supported)