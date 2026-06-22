import math

MONTHS_PER_YEAR = 12
DAYS_PER_AVERAGE_YEAR = 365.2425
DAYS_PER_AVERAGE_MONTH = DAYS_PER_AVERAGE_YEAR / MONTHS_PER_YEAR
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTE = 60

SECONDS_PER_AVERAGE_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
SECONDS_PER_AVERAGE_MONTH = DAYS_PER_AVERAGE_MONTH * SECONDS_PER_AVERAGE_DAY
SECONDS_PER_AVERAGE_YEAR = DAYS_PER_AVERAGE_YEAR * SECONDS_PER_AVERAGE_DAY

def years_to_seconds(years):
    return years * SECONDS_PER_AVERAGE_YEAR

def months_to_seconds(months):
    return months * SECONDS_PER_AVERAGE_MONTH

def days_to_seconds(days):
    return days * SECONDS_PER_AVERAGE_DAY

def hours_to_seconds(hours):
    return hours * 3600

def minutes_to_seconds(minutes):
    return minutes * 60

def seconds_to_seconds(seconds):
    return seconds

def convert_from_years(source_value):
    return years_to_seconds(source_value)

def convert_from_months(source_value):
    return months_to_seconds(source_value)

def convert_from_days(source_value):
    return days_to_seconds(source_value)

def convert_from_hours(source_value):
    return hours_to_seconds(source_value)

def convert_from_minutes(source_value):
    return minutes_to_seconds(source_value)

def convert_from_seconds(source_value):
    return seconds_to_seconds(source_value)

def seconds_to_years(seconds):
    return seconds / SECONDS_PER_AVERAGE_YEAR

def seconds_to_months(seconds):
    return seconds / SECONDS_PER_AVERAGE_MONTH

def seconds_to_days(seconds):
    return seconds / SECONDS_PER_AVERAGE_DAY

def seconds_to_hours(seconds):
    return seconds / 3600

def seconds_to_minutes(seconds):
    return seconds / 60

def seconds_to_seconds_val(seconds):
    return seconds

def convert_to_years(source_seconds):
    return seconds_to_years(source_seconds)

def convert_to_months(source_seconds):
    return seconds_to_months(source_seconds)

def convert_to_days(source_seconds):
    return seconds_to_days(source_seconds)

def convert_to_hours(source_seconds):
    return seconds_to_hours(source_seconds)

def convert_to_minutes(source_seconds):
    return seconds_to_minutes(source_seconds)

def convert_to_seconds(source_seconds):
    return seconds_to_seconds_val(source_seconds)

def convert_time(value, from_unit, to_unit):
    conversion_from = {
        'years': years_to_seconds,
        'months': months_to_seconds,
        'days': days_to_seconds,
        'hours': hours_to_seconds,
        'minutes': minutes_to_seconds,
        'seconds': seconds_to_seconds,
    }
    conversion_to = {
        'years': seconds_to_years,
        'months': seconds_to_months,
        'days': seconds_to_days,
        'hours': seconds_to_hours,
        'minutes': seconds_to_minutes,
        'seconds': seconds_to_seconds_val,
    }
    
    if from_unit not in conversion_from:
        raise ValueError(f"Unknown source unit: {from_unit}")
    if to_unit not in conversion_to:
        raise ValueError(f"Unknown target unit: {to_unit}")
    
    seconds_value = conversion_from[from_unit](value)
    result = conversion_to[to_unit](seconds_value)
    return result

def main():
    val = 1.5
    unit_from = 'years'
    unit_to = 'days'
    
    result = convert_time(val, unit_from, unit_to)
    print(f"{val} {unit_from} is {result} {unit_to}")

    val = 365
    unit_from = 'days'
    unit_to = 'years'
    
    result = convert_time(val, unit_from, unit_to)
    print(f"{val} {unit_from} is {result} {unit_to}")

    val = 100
    unit_from = 'minutes'
    unit_to = 'seconds'
    
    result = convert_time(val, unit_from, unit_to)
    print(f"{val} {unit_from} is {result} {unit_to}")

if __name__ == '__main__':
    main()