import math
def convert_to_seconds(value, unit):
    if unit == 'year':
        return value * 365.25 * 24 * 60 * 60
    elif unit == 'month':
        return value * 30.44 * 24 * 60 * 60
    elif unit == 'day':
        return value * 24 * 60 * 60
    elif unit == 'hour':
        return value * 60 * 60
    elif unit == 'minute':
        return value * 60
    elif unit == 'second':
        return value
    else:
        raise ValueError("Invalid unit specified")
def convert_from_seconds(seconds, unit):
    if unit == 'year':
        return seconds / (365.25 * 24 * 60 * 60)
    elif unit == 'month':
        return seconds / (30.44 * 24 * 60 * 60)
    elif unit == 'day':
        return seconds / (24 * 60 * 60)
    elif unit == 'hour':
        return seconds / (60 * 60)
    elif unit == 'minute':
        return seconds / 60
    elif unit == 'second':
        return seconds
    else:
        raise ValueError("Invalid unit specified")
if __name__ == '__main__':
    sample_years = 2
    sample_months = 6
    sample_days = 10
    sample_hours = 14
    sample_minutes = 30
    sample_seconds = 5
    print(f"--- Conversion Tests ---")
    seconds_from_year = convert_to_seconds(sample_years, 'year')
    print(f"{sample_years} years is approximately {seconds_from_year:.2f} seconds")
    seconds_from_month = convert_to_seconds(sample_months, 'month')
    print(f"{sample_months} months is approximately {seconds_from_month:.2f} seconds")
    seconds_from_day = convert_to_seconds(sample_days, 'day')
    print(f"{sample_days} days is approximately {seconds_from_day:.2f} seconds")
    seconds_from_hour = convert_to_seconds(sample_hours, 'hour')
    print(f"{sample_hours} hours is approximately {seconds_from_hour:.2f} seconds")
    seconds_from_minute = convert_to_seconds(sample_minutes, 'minute')
    print(f"{sample_minutes} minutes is approximately {seconds_from_minute:.2f} seconds")
    seconds_from_second = convert_to_seconds(sample_seconds, 'second')
    print(f"{sample_seconds} seconds is approximately {seconds_from_second:.2f} seconds")
    print("\n--- Reverse Conversion Tests ---")
    years_from_seconds = convert_from_seconds(seconds_from_year, 'year')
    print(f"{seconds_from_year:.2f} seconds is approximately {years_from_seconds:.2f} years")
    months_from_seconds = convert_from_seconds(seconds_from_month, 'month')
    print(f"{seconds_from_month:.2f} seconds is approximately {months_from_seconds:.2f} months")
    days_from_seconds = convert_from_seconds(seconds_from_day, 'day')
    print(f"{seconds_from_day:.2f} seconds is approximately {days_from_seconds:.2f} days")
    hours_from_seconds = convert_from_seconds(seconds_from_hour, 'hour')
    print(f"{seconds_from_hour:.2f} seconds is approximately {hours_from_seconds:.2f} hours")
    minutes_from_seconds = convert_from_seconds(seconds_from_minute, 'minute')
    print(f"{seconds_from_minute:.2f} seconds is approximately {minutes_from_seconds:.2f} minutes")
    seconds_from_second_rev = convert_from_seconds(seconds_from_second, 'second')
    print(f"{seconds_from_second:.2f} seconds is approximately {seconds_from_second_rev:.2f} seconds")