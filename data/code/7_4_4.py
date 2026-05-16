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
    print("--- Time Unit Conversion Module ---")
    print(f"\nSample Input:")
    print(f"Years: {sample_years}")
    print(f"Months: {sample_months}")
    print(f"Days: {sample_days}")
    print(f"Hours: {sample_hours}")
    print(f"Minutes: {sample_minutes}")
    print(f"Seconds: {sample_seconds}")
    print("\nConversion to Seconds:")
    seconds_from_year = convert_to_seconds(sample_years, 'year')
    print(f"{sample_years} years in seconds: {seconds_from_year:.2f}")
    seconds_from_month = convert_to_seconds(sample_months, 'month')
    print(f"{sample_months} months in seconds: {seconds_from_month:.2f}")
    seconds_from_day = convert_to_seconds(sample_days, 'day')
    print(f"{sample_days} days in seconds: {seconds_from_day:.2f}")
    seconds_from_hour = convert_to_seconds(sample_hours, 'hour')
    print(f"{sample_hours} hours in seconds: {seconds_from_hour:.2f}")
    seconds_from_minute = convert_to_seconds(sample_minutes, 'minute')
    print(f"{sample_minutes} minutes in seconds: {seconds_from_minute:.2f}")
    seconds_from_second = convert_to_seconds(sample_seconds, 'second')
    print(f"{sample_seconds} seconds in seconds: {seconds_from_second:.2f}")
    print("\nConversion from Seconds:")
    result_years = convert_from_seconds(seconds_from_year, 'year')
    print(f"{seconds_from_year:.2f} seconds converted to years: {result_years:.4f}")
    result_months = convert_from_seconds(seconds_from_month, 'month')
    print(f"{seconds_from_month:.2f} seconds converted to months: {result_months:.4f}")
    result_days = convert_from_seconds(seconds_from_day, 'day')
    print(f"{seconds_from_day:.2f} seconds converted to days: {result_days:.4f}")
    result_hours = convert_from_seconds(seconds_from_hour, 'hour')
    print(f"{seconds_from_hour:.2f} seconds converted to hours: {result_hours:.4f}")
    result_minutes = convert_from_seconds(seconds_from_minute, 'minute')
    print(f"{seconds_from_minute:.2f} seconds converted to minutes: {result_minutes:.4f}")
    result_seconds = convert_from_seconds(seconds_from_second, 'second')
    print(f"{seconds_from_second:.2f} seconds converted to seconds: {result_seconds:.2f}")