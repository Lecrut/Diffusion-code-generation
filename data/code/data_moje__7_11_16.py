class TimeConverter:
    _BASES = {
        'nanoseconds': 1e-9,
        'microseconds': 1e-6,
        'milliseconds': 1e-3,
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,
        'weeks': 604800,
        'years': 31536000
    }

    def __init__(self):
        self._current_base = 1

    def get_factor(self, unit):
        unit_lower = unit.lower()
        if unit_lower not in self._BASES:
            raise KeyError(f"Unknown time unit: {unit}")
        return self._BASES[unit_lower]

    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric")
        
        from_factor = self.get_factor(from_unit)
        to_factor = self.get_factor(to_unit)
        
        base_value = value * from_factor
        result = base_value / to_factor
        
        if result == int(result):
            return int(result)
        
        return result

    def get_current_base(self):
        return self._current_base

    def set_base(self, unit):
        factor = self.get_factor(unit)
        self._current_base = factor

if __name__ == '__main__':
    converter = TimeConverter()
    
    result_seconds_to_minutes = converter.convert(3600, 'seconds', 'minutes')
    print(result_seconds_to_minutes)
    
    result_hours_to_days = converter.convert(24, 'hours', 'days')
    print(result_hours_to_days)
    
    result_days_to_hours = converter.convert(2, 'days', 'hours')
    print(result_days_to_hours)
    
    result_weeks_to_seconds = converter.convert(1, 'weeks', 'seconds')
    print(result_weeks_to_seconds)