import math

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600
SECONDS_IN_DAY = 86400
SECONDS_IN_YEAR = 31557600
SECONDS_IN_MONTH = 2629800

def convert(source_value, source_unit, target_unit):
    source_unit = source_unit.lower()
    target_unit = target_unit.lower()
    valid_units = ['year', 'month', 'day', 'hour', 'minute', 'second']
    
    if source_unit not in valid_units or target_unit not in valid_units:
        raise ValueError(f"Invalid unit. Valid units are: {', '.join(valid_units)}")
    
    if source_unit == 'year':
        seconds = source_value * SECONDS_IN_YEAR
    elif source_unit == 'month':
        seconds = source_value * SECONDS_IN_MONTH
    elif source_unit == 'day':
        seconds = source_value * SECONDS_IN_DAY
    elif source_unit == 'hour':
        seconds = source_value * SECONDS_IN_HOUR
    elif source_unit == 'minute':
        seconds = source_value * SECONDS_IN_MINUTE
    else:
        seconds = source_value
    
    if target_unit == 'year':
        return seconds / SECONDS_IN_YEAR
    elif target_unit == 'month':
        return seconds / SECONDS_IN_MONTH
    elif target_unit == 'day':
        return seconds / SECONDS_IN_DAY
    elif target_unit == 'hour':
        return seconds / SECONDS_IN_HOUR
    elif target_unit == 'minute':
        return seconds / SECONDS_IN_MINUTE
    else:
        return seconds

class TimeConverter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit.lower()
    
    def to(self, target_unit):
        return convert(self.value, self.unit, target_unit)
    
    def to_all(self):
        units = ['year', 'month', 'day', 'hour', 'minute', 'second']
        results = {}
        for unit in units:
            results[unit] = convert(self.value, self.unit, unit)
        return results

if __name__ == '__main__':
    sample_value = 2
    sample_unit = 'years'
    target_unit = 'days'
    
    direct_result = convert(sample_value, sample_unit, target_unit)
    print(f"{sample_value} {sample_unit} is {direct_result} {target_unit}")
    
    converter = TimeConverter(1, 'hour')
    minute_result = converter.to('minute')
    print(f"1 hour is {minute_result} minutes")
    
    all_conversions = converter.to_all()
    print(f"1 hour in all units: {all_conversions}")