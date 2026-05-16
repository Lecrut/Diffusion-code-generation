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
    sample_days = 15
    sample_hours = 10
    sample_minutes = 30
    sample_seconds = 45
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
    print(f"{sample_seconds} seconds is {seconds_from_second:.2f} seconds")
    print("\n--- Reverse Conversions (Starting from a known total) ---")
    total_seconds = 86400 * 365.25 * 2 + 10 * 3600 + 30 * 60 + 45
    print(f"Total seconds calculated: {total_seconds:.2f}")
    years_back = convert_from_seconds(total_seconds, 'year')
    print(f"Total seconds converted back to years: {years_back:.2f}")
    total_seconds_month = 30.44 * 24 * 60 * 60 * 6 + 15 * 24 * 60 * 60 + 10 * 3600 + 30 * 60 + 45
    print(f"Total seconds for months/days/hours/minutes/seconds: {total_seconds_month:.2f}")
    months_back = convert_from_seconds(total_seconds_month, 'month')
    print(f"Total seconds converted back to months: {months_back:.2f}")