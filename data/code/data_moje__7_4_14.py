import math

AVERAGE_DAYS_PER_YEAR = 365.2425
AVERAGE_DAYS_PER_MONTH = 30.436875

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_YEAR = AVERAGE_DAYS_PER_YEAR
DAYS_IN_MONTH = AVERAGE_DAYS_PER_MONTH

MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY
SECONDS_IN_HOUR = MINUTES_IN_HOUR * SECONDS_IN_MINUTE
SECONDS_IN_DAY = HOURS_IN_DAY * MINUTES_IN_DAY

def convert_seconds_to_other_units(total_seconds):
    total_minutes = total_seconds / SECONDS_IN_MINUTE
    total_hours = total_seconds / SECONDS_IN_HOUR
    total_days = total_seconds / SECONDS_IN_DAY
    total_months = total_seconds / (SECONDS_IN_DAY * DAYS_IN_MONTH)
    total_years = total_seconds / (SECONDS_IN_DAY * DAYS_IN_YEAR)
    return {
        "years": total_years,
        "months": total_months,
        "days": total_days,
        "hours": total_hours,
        "minutes": total_minutes,
        "seconds": total_seconds
    }

def convert_any_to_seconds(value, unit):
    unit = unit.lower()
    if unit == "year" or unit == "years":
        return value * DAYS_IN_YEAR * SECONDS_IN_DAY
    elif unit == "month" or unit == "months":
        return value * DAYS_IN_MONTH * SECONDS_IN_DAY
    elif unit == "day" or unit == "days":
        return value * SECONDS_IN_DAY
    elif unit == "hour" or unit == "hours":
        return value * SECONDS_IN_HOUR
    elif unit == "minute" or unit == "minutes":
        return value * SECONDS_IN_MINUTE
    elif unit == "second" or unit == "seconds":
        return value
    else:
        raise ValueError(f"Unknown time unit: {unit}")

def convert_between_units(value, from_unit, to_unit):
    seconds_value = convert_any_to_seconds(value, from_unit)
    result_seconds = convert_seconds_to_other_units(seconds_value)
    
    to_unit = to_unit.lower()
    if to_unit == "year" or to_unit == "years":
        return result_seconds["years"]
    elif to_unit == "month" or to_unit == "months":
        return result_seconds["months"]
    elif to_unit == "day" or to_unit == "days":
        return result_seconds["days"]
    elif to_unit == "hour" or to_unit == "hours":
        return result_seconds["hours"]
    elif to_unit == "minute" or to_unit == "minutes":
        return result_seconds["minutes"]
    elif to_unit == "second" or to_unit == "seconds":
        return result_seconds["seconds"]
    else:
        raise ValueError(f"Unknown target unit: {to_unit}")

class TimeConverter:
    def __init__(self):
        self.cache = {}

    def convert(self, value, from_unit, to_unit):
        return convert_between_units(value, from_unit, to_unit)

    def decompose_to_all_units(self, value, from_unit):
        seconds_value = convert_any_to_seconds(value, from_unit)
        return convert_seconds_to_other_units(seconds_value)

    def convert_years_to_months(self, years):
        return years * DAYS_IN_YEAR / DAYS_IN_MONTH

    def convert_days_to_hours(self, days):
        return days * HOURS_IN_DAY

    def convert_minutes_to_seconds(self, minutes):
        return minutes * SECONDS_IN_MINUTE

if __name__ == '__main__':
    converter = TimeConverter()
    
    years_result = converter.convert(2.5, "years", "days")
    print(years_result)
    
    months_result = converter.convert(180, "days", "hours")
    print(months_result)
    
    seconds_result = converter.convert(3600, "seconds", "minutes")
    print(seconds_result)
    
    all_units_result = converter.decompose_to_all_units(1, "year")
    print(all_units_result)
    
    specific_months = converter.convert_years_to_months(5)
    print(specific_months)
    
    specific_hours = converter.convert_days_to_hours(7)
    print(specific_hours)
    
    specific_seconds = converter.convert_minutes_to_seconds(45)
    print(specific_seconds)
    
    mixed_test = converter.convert(1000000, "seconds", "days")
    print(mixed_test)