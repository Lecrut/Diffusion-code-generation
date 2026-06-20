import math

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
DAYS_PER_MONTH_AVG = 30.4375
MONTHS_PER_YEAR_AVG = 12.0
SECONDS_PER_HOUR = HOURS_PER_DAY * SECONDS_PER_MINUTE
SECONDS_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
SECONDS_PER_MONTH = int(SECONDS_PER_DAY * DAYS_PER_MONTH_AVG)
SECONDS_PER_YEAR = int(SECONDS_PER_DAY * DAYS_PER_MONTH_AVG * MONTHS_PER_YEAR_AVG)

class TimeConverter:
    def __init__(self):
        self.units = {
            'year': SECONDS_PER_YEAR,
            'month': SECONDS_PER_MONTH,
            'day': SECONDS_PER_DAY,
            'hour': SECONDS_PER_HOUR,
            'minute': SECONDS_PER_MINUTE,
            'second': 1
        }

    def convert(self, value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in self.units:
            raise ValueError(f"Invalid source unit: {from_unit}")
        if to_unit not in self.units:
            raise ValueError(f"Invalid target unit: {to_unit}")
        
        seconds = value * self.units[from_unit]
        result = seconds / self.units[to_unit]
        return result

    def convert_all(self, value, from_unit):
        from_unit = from_unit.lower()
        if from_unit not in self.units:
            raise ValueError(f"Invalid source unit: {from_unit}")
        
        seconds = value * self.units[from_unit]
        results = {}
        for unit_name, unit_seconds in self.units.items():
            results[unit_name] = seconds / unit_seconds
        return results

if __name__ == '__main__':
    converter = TimeConverter()
    
    test_value = 1
    test_from = 'day'
    test_to = 'hour'
    result = converter.convert(test_value, test_from, test_to)
    print(f"Converting {test_value} {test_from} to {test_to}: {result}")
    
    test_value_year = 1
    test_from_year = 'year'
    test_to_year = 'second'
    result_year = converter.convert(test_value_year, test_from_year, test_to_year)
    print(f"Converting {test_value_year} {test_from_year} to {test_to_year}: {result_year}")
    
    test_value_hour = 2.5
    test_from_hour = 'hour'
    test_to_hour = 'minute'
    result_hour = converter.convert(test_value_hour, test_from_hour, test_to_hour)
    print(f"Converting {test_value_hour} {test_from_hour} to {test_to_hour}: {result_hour}")
    
    test_value_month = 1
    test_from_month = 'month'
    test_to_month = 'day'
    result_month = converter.convert(test_value_month, test_from_month, test_to_month)
    print(f"Converting {test_value_month} {test_from_month} to {test_to_month}: {result_month}")
    
    test_value_second = 86400
    test_from_second = 'second'
    test_to_second = 'day'
    result_second = converter.convert(test_value_second, test_from_second, test_to_second)
    print(f"Converting {test_value_second} {test_from_second} to {test_to_second}: {result_second}")
    
    all_results = converter.convert_all(1, 'year')
    print("Converting 1 year to all units:", all_results)