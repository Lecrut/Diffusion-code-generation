from decimal import Decimal
from typing import Union

AVERAGE_DAYS_IN_YEAR = 365.2425
AVERAGE_DAYS_IN_MONTH = 30.436875

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_WEEK = 7

def get_base_factor(unit: str) -> Decimal:
    unit_lower = unit.lower()
    if unit_lower in ('s', 'sec', 'second', 'seconds'):
        return Decimal('1')
    elif unit_lower in ('m', 'min', 'minute', 'minutes'):
        return Decimal(SECONDS_IN_MINUTE)
    elif unit_lower in ('h', 'hr', 'hour', 'hours'):
        return Decimal(SECONDS_IN_MINUTE * MINUTES_IN_HOUR)
    elif unit_lower in ('d', 'day', 'days'):
        return Decimal(SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY)
    elif unit_lower in ('w', 'week', 'weeks'):
        return Decimal(SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY * DAYS_IN_WEEK)
    elif unit_lower in ('mo', 'month', 'months'):
        return Decimal(SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY * AVERAGE_DAYS_IN_MONTH)
    elif unit_lower in ('y', 'yr', 'year', 'years'):
        return Decimal(SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY * AVERAGE_DAYS_IN_YEAR)
    else:
        raise ValueError(f"Unknown time unit: {unit}")

def convert_time(value: Union[int, float], from_unit: str, to_unit: str) -> Decimal:
    if from_unit.lower() == to_unit.lower():
        return Decimal(str(value))
    
    from_factor = get_base_factor(from_unit)
    to_factor = get_base_factor(to_unit)
    
    base_value = Decimal(str(value)) * from_factor
    result = base_value / to_factor
    return result

class TimeConverter:
    def __init__(self):
        self.conversion_map = {
            'years': 'years', 'years': 'years',
            'months': 'months',
            'days': 'days',
            'hours': 'hours',
            'minutes': 'minutes',
            'seconds': 'seconds'
        }

    def convert(self, amount: float, from_unit: str, to_unit: str) -> float:
        result = convert_time(amount, from_unit, to_unit)
        return float(result)

    def convert_all_units(self, amount: float, from_unit: str) -> dict:
        target_units = ['years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds']
        results = {}
        for unit in target_units:
            results[unit] = self.convert(amount, from_unit, unit)
        return results

if __name__ == '__main__':
    converter = TimeConverter()
    input_amount = 1
    input_unit = 'years'
    target_unit = 'days'
    converted_value = converter.convert(input_amount, input_unit, target_unit)
    print(f"{input_amount} {input_unit} equals {converted_value} {target_unit}")
    all_conversions = converter.convert_all_units(1, 'hours')
    print(f"1 hour in all units: {all_conversions}")